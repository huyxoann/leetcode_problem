# Best time to buy and sell stock
Sử dụng biến min_price biểu thị dương vô cùng và max_profit bằng 0
Duyệt từng phần tử trong mảng prices:
    - so sánh giá và giá nhỏ nhất để lưu lại giá mua nhỏ hơn
    - ngược lại, sẽ tính xem giá đó trừ giá nhỏ nhất có lớn hơn lợi nhuận lớn nhất hay không để xác định giá lời nhất.

# Climbing stairs
Mảng lưu giá trị:
    index: số bậc thang hiện tại
    value: bao nhiêu cách để đi với số index bậc thang
Duyệt mảng để lưu các giá trị và trả về element cuối cùng

# First occurrence in string
Kiểm tra chuỗi needle: Nếu needle rỗng, hàm trả về 0.
Duyệt haystack: Hàm lặp qua các vị trí trong haystack từ 0 đến (len(haystack) - len(needle) + 1).
So sánh chuỗi con: Tại mỗi vị trí, nó kiểm tra liệu đoạn chuỗi từ vị trí đó dài bằng len(needle) có trùng với needle hay không.
Trả về kết quả: Nếu trùng, trả về chỉ số đầu tiên của needle trong haystack. Nếu hết vòng lặp mà không tìm thấy, trả về -1.

# Length of last word
Tách chuỗi thành list các chuỗi và trả về độ dài chuỗi cuối cùng

# Longest Common Prefix
Duyệt qua các ký tự trong chuỗi đầu tiên (strs[0]): Giả sử chuỗi đầu tiên là tiền tố chung, hàm duyệt qua từng ký tự trong chuỗi này.
So sánh với các chuỗi còn lại: Với mỗi ký tự i trong strs[0], hàm kiểm tra:
Nếu ký tự tại vị trí i trong bất kỳ chuỗi nào khác không khớp với strs[0][i], hoặc nếu vị trí đó vượt quá độ dài của chuỗi đó, hàm sẽ in ra tiền tố chung đến thời điểm đó (strs[0][:i]).
Kết quả trả về: Cuối cùng, hàm trả về toàn bộ chuỗi strs[0].

# Maximum depth of binary tree
Sử dụng đệ quy trả về độ sâu lớn nhất giữa nhánh trái và nhánh phải + 1

# Merge 2 sorted list
Sử dụng đệ quy lần lượt kiểm tra giá trị giữa hai node, từ đó vẽ đường dẫn từ để ghép 2 list theo giá trị tăng dần

# Palindrome
Lần lượt duyệt qua chuỗi và gán các kí tự vào trước chuỗi kết quả rồi kiểm tra chuỗi ban đầu với kết quả có giống nhau.

# Remove duplicate fromm sorted list
Lần lượt kiếm tra node hiện tại vào node kế tiếp nó có giá trị giống nhau không, nếu có thì bỏ qua node đó và nối đến node tiếp theo

# Remove duplicate from sorted array 
Duyệt mảng để kiểm tra nếu giá trị ở phần tử i khác các phần từ j kế tiếp nó, nếu có thì sẽ tăng i lên 1 và ghi đè phần tử ở j vào phần tử ở i.

# Remove element
Duyệt mảng để xem giá trị ở phần tử i có bằng target, nếu khác target, ghi đè giá trị ở phần tử i vào giá trị ở phần tử k và tăng k lên 1, làm cho các phần từ có giá trị bằng target bị ghi đè lên.

# Roman to integer 
Duyệt chuỗi roman s, với mối kí tự trong s, kiểm tra trong dictionary để xem giá trị của nó bằng bao nhiều.
So sánh nếu kí tự la mã a đó đứng trước kí tự la mã a+1 có giá trị lớn hơn: lấy tổng từ cho giá trị của a, ngược lại lấy tổng cộng cho giá trị của a.

# Same tree
Dùng đệ quy duyệt cây và so sánh nhánh trái của từng node ở cây p, q có giống nhánh phải của từng node ở cây p, q. Từ đó suy ra được toàn bộ cây p, q có giống nhau không

# Search Insert position
duyệt mảng số và so sánh nếu số đó lớn hơn hoặc bằng target, nếu đúng trả về vị trí của số đó, làm được điều này vì mảng đã được sắp xếp rồi.

# Single number
Duyệt mảng các số trong nums và dùng set count để lưu các giá trị đã xuất hiện, 
nếu số tiếp theo trong mảng đã xuất hiện trong count, gán bằng 1
Sau cùng kiểm tra xem có số nào bằng 1 trong set => số duy nhất.

# Sqrt x
Sử dụng toán tử ** (số mũ), x mũ 0.5 bằng căn của x

# Symmetric tree
Bài toán kiếm tra xem cây này có nhánh trái và nhánh phải đối xứng nhau.
Sử dụng đệ quy để kiểm tra xem với mỗi nhánh, phía bên trái trái có giống phía bên phải nhánh phải hay không và ngược lại.

# Two sum
Duyệt các phần tử để kiểm tra xem target - số đang duyệt có nằm trong set d hay không, vì enumerate có cấu trúc index: num nên có thể biết được vị trí của hai số để trả về.

# Valid palindrome
Lọc các kí tự chữ cái thường và số, tạo thành 1 chuỗi,
tạo chuỗi mới bằng cách duyệt ngược chuỗi trên bằng [::-1], rồi so sánh hai chuỗi đó.

# Valid parentheses
Sử dụng stack để lưu các kí tự được duyệt, 
Duyệt các ký tự chuỗi trong chuỗi s, kiểm tra tính hợp lệ dựa vào set mapping: ví dụ như mở ngoặc { thì phải có đóng ngoặc } liền kề.
Valid parentheses nếu sau cùng, stack được trống hết.