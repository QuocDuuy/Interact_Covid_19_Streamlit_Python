# Building a Covid-19 Dashboard using streamlit pyton
## >> Streamlit là một thư viện python mã nguồn mở cho phép chúng tôi tạo các trang tổng quan đẹp, có tính tương tác cao và nhiều thông tin một cách dễ dàng. Nó cũng cho phép chúng tôi tạo các ứng dụng Học máy và Khoa học dữ liệu dựa trên tùy chỉnh.

## >> Ở đây ta sẽ sử dụng công cụ là jupyter notebook - python 3

## >> Để tạo nên một dashboard thật đẹp trên một localhost ta sẽ làm các bước sau:
#
## Bước 1: Cài đặt thư viện streamlit
## >>> Khởi động chương trình anaconda3 Powershell Prompt lên
## >>> Nhập câu lệnh sau:
    pip install streamlit
## >>> Nhập vào terminal:
    streamlit hello
## >>> Lưu ý: Có một thư viện sẽ báo lỗi (wordcloud)
## >>> Khắc phục: Bật anaconda3 Powershell Prompt lên, gõ vào dòng lệnh
    conda install wordcloud
## >>> Sau đó ta tiếp tục với câu lệnh:
    pip install wordcloud
## hoặc là
    pip3 install wordcloud
## Sau đó chúng ta sẽ thực hiện chương trình trực quan hóa dashboard trên một localhost
## A. Implementation
## >>> Import các thư viện cần thiết
## >>> Import các dataset vào
## B. Starting with setting the title and the sidebar title for streamlit dashboard
## >>> Visualization (part-1: vẽ biểu đồ cột và biểu đồ tròn)
## >>> Visualization (part-2: active và confirmed trên chuỗi thời gian)
## >>> Visualization (part-3: vẽ biểu đồ khu vực)
## -------------------------------------------------------------------------
## Lưu ý: Muốn code trên jupyter notebook hoạt động thì ta sẽ bật anaconda3 Powershell Prompt lần nữa và đánh vào dòng lệnh sau:
    streamlit run 'path/app_name.py'
## >>> path: là đường dẫn tới file .py hiện hành (VD: C:/Users/ntmth/Data Science/Interactive-Dashboards-With-Streamlit/...)
## >>> app_name.py: là một file .py chứa code hiện hành (sau khi mình thao tác code trên jupyter notebook xong, mình sẽ download as file source code này về với dạng .py vì streamlit chỉ nhận file có đuôi .py và phải lưu file .py ấy cùng với thư mục hiện hành)
## >>> Lưu ý nhớ đường dẫn phải nằm trong dấu nháy đơn như câu lệnh trên nhé!

# REFERENCE
1. Trang hướng dẫn code: https://analyticsindiamag.com/building-a-covid-19-dashboard-using-streamlit/
2. Database mẫu: https://data.covid19india.org/

#
## *CHÚC CÁC BẠN THÀNH CÔNG NHÉ! CODE NEVER DIEEEEEEE!!!*
