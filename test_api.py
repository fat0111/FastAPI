import requests

url = "http://127.0.0.1:8000/generate"

# Thử nghiệm với 2 địa điểm khác nhau
test_cases = [
    {"location": "Chùa Một Cột", "max_new_tokens": 150},
    {"location": "Hang Sơn Đoòng", "max_new_tokens": 150}
]

print("--- BẮT ĐẦU KIỂM THỬ API QWEN0.5 ---")

for i, data in enumerate(test_cases, 1):
    try:
        response = requests.post(url, json=data)
        
        print(f"\n[Lần thử {i}]")
        print(f"Địa điểm gửi đi: {data['location']}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Hướng dẫn viên AI phản hồi:\n{result['blind_box_hint']}")
        else:
            print(f"Lỗi {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"Không thể kết nối đến API: {e}")

print("\n--- KẾT THÚC KIỂM THỬ ---")