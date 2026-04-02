from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import pipeline

app = FastAPI()

print("Đang tải mô hình Qwen2.5-0.5B-Instruct... (có thể mất vài phút)")
# Cấu hình tải mô hình: Dùng torch.float16 và device_map="auto" để tối ưu RAM/VRAM
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct", 
    torch_dtype=torch.float16,
    device_map="auto" 
)
print("Tải mô hình thành công!")
class PromptData(BaseModel):
    location: str
    max_new_tokens: int = 150 # Số từ tối đa AI được phép trả lời

@app.get("/")
def read_root():
    return {"project": "Blind Box Travelling", "model": "Qwen2.5-0.5B-Instruct"}

@app.get("/health")
def health_check():
    return {"status": "hoạt động tốt"}

@app.post("/generate")
def generate_text(data: PromptData):
    try:
        # Prompt đơn giản như lúc đầu bạn muốn
        messages = [
            {"role": "system", "content": "Bạn là hướng dẫn viên du lịch. Hãy viết 3-4 câu mô tả hấp dẫn về địa điểm được cung cấp. Chỉ mô tả địa điểm, không tự bịa vị trí hay vùng của địa điểm đó. Không chào hỏi."},
            {"role": "user", "content": f"Viết mô tả cho: {data.location}"}
        ]

        # Để temperature vừa phải để nó không bị 'điên'
        result = pipe(
            messages, 
            max_new_tokens=150, 
            do_sample=True, 
            temperature=0.5, 
            top_p=0.9
        )
        ai_response = result[0]["generated_text"][-1]["content"]


        final_text = ai_response.replace(data.location, "Địa điểm này")
        
        # 2. Làm sạch các ký tự lạ hoặc khoảng trắng thừa
        final_text = final_text.strip()

        return {
            "location": data.location,
            "blind_box_hint": final_text
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))