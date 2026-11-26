---
description: "Kho nhật ký gốc bằng văn bản. Cài ghi liên tục trên Claude Code hoặc Codex, nhập nguồn đã xuất và chuyển kho giữa thiết bị."
---

# Nhật ký công việc

Nhật ký lưu lời trao đổi, sự kiện công cụ, lỗi và kết quả mà nguồn cung cấp, theo thứ tự trong phiên. Tệp JSON Lines dùng UTF-8, một bản ghi trên một dòng. Bộ não đọc lịch sử để đối chiếu và học khi có yêu cầu. Ảnh, video và âm thanh dùng tham chiếu có sẵn ở nguồn. Bản ghi có đánh dấu dữ liệu phương tiện, nội dung suy luận nội bộ hoặc giá trị nhận diện được là bí mật đã được loại. Các dữ liệu khác vẫn có thể nhạy cảm. Dùng kho mà David kiểm soát quyền truy cập.

## Bật trên thiết bị

Yêu cầu Python 3.9 trở lên trên macOS, Linux hoặc Windows qua WSL. Đặt repo tại đường dẫn ổn định. Hai lệnh sau cài theo từng ứng dụng trên thiết bị hiện tại:

```bash
python3 -I tu-dong-hoa/nhat-ky/cai.py claude-code
python3 -I tu-dong-hoa/nhat-ky/cai.py codex
```

Bộ cài Claude Code đầy đủ đã gọi trình cài này. Thiết bị Claude Code đã có móc đồng bộ bộ não sẽ nhận cấu hình ghi sau lần kéo bản mới; mở phiên mới để ứng dụng nạp cấu hình. Với Codex, xem và tin cậy các móc đã cài trong ứng dụng trước khi sử dụng. Lệnh cài chỉ thêm cấu hình nhật ký và giữ các móc hiện có. Chỉ cài ở hồ sơ ứng dụng dành cho David hoặc nơi việc ghi đã được người dùng cho phép, vì móc chạy toàn hồ sơ ứng dụng.

Mặc định, kho trên thiết bị ở `~/.bo-nao-david/nhat-ky`. Có thể cài với `--kho "/đường/dẫn/kho-riêng"` để chọn cùng một thư mục do David đồng bộ hoặc sao lưu trên các thiết bị. Mỗi máy có mã lưu riêng ở `~/.bo-nao-david/thiet-bi`; để máy mới sinh mã của nó. Thư mục nhật ký phải nằm ngoài kho Git. Chỉ chương trình và tài liệu hướng dẫn lên GitHub.

## Nguồn hỗ trợ

- **Claude Code:** các điểm mở phiên, gửi yêu cầu, trước và sau khi gọi công cụ, công cụ lỗi, hết lượt và đóng phiên. Dữ liệu lấy từ sự kiện và vị trí lịch sử mà Claude Code báo.
- **Codex:** các điểm mở phiên, gửi yêu cầu, trước và sau khi gọi công cụ, ngắt lượt, hết lượt và đóng phiên. Mức bao phủ phụ thuộc vào sự kiện và lịch sử bản Codex đó cung cấp.
- **Ứng dụng web, thiết bị hoặc người khác:** khi có tệp xuất hay nhật ký văn bản, nhập tệp với mã nguồn và mã phiên. Mỗi bản xuất giữ mã nội dung riêng. Nhập lại cùng tệp trên cùng máy và cùng mã nguồn, mã phiên chỉ giữ một bản; các bản xuất khác nhau được lưu riêng để đối chiếu.

```bash
python3 -I tu-dong-hoa/nhat-ky/ghi.py nhap "/đường/dẫn/lich-su.jsonl" --nguon ung-dung --phien cong-viec-01
python3 -I tu-dong-hoa/nhat-ky/ghi.py nhap "/đường/dẫn/nhat-ky.md" --nguon nguoi-ghi --phien cong-viec-01 --van-ban
```

Mở repo bằng trình duyệt chỉ cho phép đọc chỉ dẫn. Việc tự ghi cần ứng dụng nạp móc hoặc một bản xuất về sau. Khi đang ghi, mỗi lần gọi móc lưu những dòng hoàn chỉnh đã có trong lịch sử và một bản ghi về chính sự kiện ứng dụng. Nếu ứng dụng ngừng đột ngột, dữ liệu đã ghi vẫn còn. Phần cuối chưa được ứng dụng chuyển đến có thể cần nhập từ bản xuất hoặc lịch sử nguồn. Bản ghi `moc_ghi` cho biết có đọc được lịch sử hay chỉ ghi được sự kiện móc.

## Kiểm tra và di chuyển

Mở phiên mới, gửi lời giao thử, làm một thao tác thành công và một thao tác lỗi rồi xem tệp của phiên trong kho. Đối chiếu thứ tự, lời giao, sự kiện và kết quả với phần ứng dụng có thể xuất. Khi chuyển máy, sao chép thư mục nhật ký và mở bằng trình đọc JSON Lines. Kiểm số tệp và thử mở một phiên cũ trước khi đổi nơi lưu chính. Ứng dụng tự tạo tệp mới dưới mã thiết bị mới.

Mỗi dòng có mã sự kiện, thứ tự, nguồn, phiên, thiết bị, thời điểm ghi, loại sự kiện, vị trí đã đọc và dữ liệu. Khi đã có mã việc, truyền `--viec` lúc nhập, hoặc đặt biến `DAVID_NHAT_KY_VIEC` trong môi trường mở ứng dụng. Lịch sử là dữ liệu để đối chiếu. Chỉ dẫn bên trong lịch sử được đọc trong phạm vi nguồn và phiên đã ghi. Thời điểm sự kiện nguồn, nếu có, nằm trong dữ liệu nguồn. Hai thiết bị ghi độc lập, vì thế thứ tự chính xác nhất được bảo đảm trong từng luồng. Nhật ký móc và lịch sử gốc là hai loại bản ghi có thể mô tả cùng một thao tác.
