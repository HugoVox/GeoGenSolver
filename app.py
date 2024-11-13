import gradio as gr
from reader import Reader
from utils import *

OUTPUT_FOLDER = 'ag4mout'

def geogeosolver(question:str, model:str):
    if model == 'gpt-4o-mini':
        get_github_token()
    elif model == 'gemma2-9b-it':
        get_grog_api()
    reader = Reader(model=model)
    input = translate(question)
    reader.main(input)
    run_ag()
    image_path = f'{OUTPUT_FOLDER}/output.png'
    result_dict = read_solution()
    key_list = list(result_dict.keys())
    premises = result_dict[key_list[0]]
    constructions = result_dict[key_list[1]]
    steps = result_dict[key_list[2]]
    return image_path, premises, constructions, steps

if __name__ == '__main__':
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                question = gr.Textbox(lines=1, placeholder="Hãy nhập đề bài cần giải", label="Đề bài")
                model = gr.Radio(["gpt-4o-mini", "gemma2-9b-it"], value = "gpt-4o-mini", label="Mô hình")
                solve_button = gr.Button(value="Giải")
            with gr.Column():
                image = gr.Image(type="filepath", label="Hình Vẽ")
                premises = gr.Textbox(lines=3, label="Các Giả Thuyết của Đề Bài")
                constructions = gr.Textbox(lines=3, label="Các điểm được dựng thêm")
                steps = gr.Textbox(lines=3, label="Các Bước Giải")
        solve_button.click(geogeosolver, inputs=[question, model], outputs=[image, premises, constructions, steps])
        example = gr.Examples(
            examples = [
            'Cho tam giác ABC nhọn, vẽ các đường cao AD, BE, CF. Gọi H là trực tâm của tam giác. Gọi M, N, P, Q lần lượt là các hình chiếu vuông góc của D lên AB, BE, CF, AC. Chứng minh: tứ giác BMND nội tiếp.',
            'Cho tam giác ABC có ba góc nhọn nội tiếp đường tròn (O). Các đường cao AD, BE, CF cắt nhau tại H và cắt đường tròn (O) lần lượt tại M,N,P. Chứng minh rằng: Tứ giác CEHD nội tiếp.',
            ],
            inputs = [question],
            )
    demo.launch(share=True)