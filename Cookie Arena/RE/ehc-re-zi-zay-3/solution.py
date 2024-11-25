from z3 import *

# Tạo một solver
solver = Solver()

# Khai báo biến cho a1 với 18 phần tử, mỗi phần tử là một số nguyên từ 0 đến 255
a1 = [Int(f'a1_{i}') for i in range(18)]
for i in range(18):
    solver.add(a1[i] >= 0, a1[i] <= 255)

# Thêm các điều kiện
solver.add(a1[15] + a1[8] + a1[3] - a1[17] - a1[12] - a1[9] - a1[6] - a1[0] - a1[2] + a1[5] == -396)
solver.add(a1[4] + a1[6] + a1[2] - a1[7] - a1[0] - a1[15] - a1[10] - a1[14] - a1[3] + a1[13] == -67)
solver.add(a1[0] + a1[17] + a1[16] + a1[2] - a1[11] - a1[3] - a1[5] - a1[4] - a1[10] + a1[1] == 82)
solver.add(a1[5] + a1[4] + a1[13] + a1[14] - a1[9] - a1[12] - a1[17] - a1[15] - a1[16] - a1[8] == -122)
solver.add(a1[3] + a1[12] + a1[6] + a1[17] + a1[13] + a1[11] - a1[4] - a1[5] - a1[9] + a1[14] == 318)
solver.add(a1[4] + a1[5] + a1[12] + a1[6] + a1[15] + a1[0] + a1[3] + a1[17] - a1[10] - a1[14] == 552)
solver.add(a1[10] + a1[12] + a1[9] + a1[13] + a1[4] + a1[17] + a1[6] - a1[11] - a1[8] - a1[1] == 577)
solver.add(a1[6] + a1[10] + a1[0] + a1[3] - a1[15] - a1[13] - a1[5] - a1[11] - a1[1] + a1[2] == 119)
solver.add(a1[2] + a1[0] + a1[9] + a1[6] + a1[5] - a1[8] - a1[1] - a1[7] - a1[12] - a1[13] == 157)
solver.add(a1[13] + a1[6] + a1[2] + a1[15] + a1[5] + a1[0] - a1[17] - a1[11] - a1[3] - a1[8] == 309)
solver.add(a1[1] + a1[2] + a1[0] - a1[8] - a1[10] - a1[15] - a1[16] - a1[12] - a1[7] - a1[5] == -302)
solver.add(a1[17] + a1[5] + a1[12] + a1[15] - a1[7] - a1[4] - a1[0] - a1[11] - a1[3] + a1[9] == 81)
solver.add(a1[11] + a1[14] + a1[12] - a1[9] - a1[2] - a1[10] - a1[15] - a1[1] - a1[17] + a1[7] == -172)
solver.add(a1[9] + a1[17] + a1[0] + a1[13] + a1[11] - a1[10] - a1[5] - a1[4] - a1[8] + a1[12] == 236)
solver.add(a1[3] + a1[17] + a1[2] - a1[0] - a1[16] - a1[5] - a1[10] - a1[14] - a1[1] + a1[12] == -224)
solver.add(a1[12] + a1[4] + a1[13] + a1[5] + a1[10] - a1[6] - a1[2] - a1[8] - a1[7] - a1[9] == 122)
solver.add(a1[11] + a1[13] + a1[15] + a1[16] + a1[4] - a1[1] - a1[2] - a1[5] - a1[12] + a1[3] == 122)
solver.add(a1[14] + a1[15] + a1[12] + a1[10] + a1[9] - a1[8] - a1[1] - a1[6] - a1[3] + a1[4] == 336)
solver.add(a1[14] + a1[12] + a1[9] + a1[10] - a1[15] - a1[2] - a1[8] - a1[4] - a1[13] - a1[11] == -37)
solver.add(a1[2] + a1[10] + a1[14] + a1[17] + a1[8] + a1[0] + a1[7] - a1[9] - a1[1] - a1[4] == 355)
solver.add(a1[17] + a1[1] + a1[15] + a1[8] + a1[14] + a1[16] + a1[0] - a1[3] - a1[11] + a1[13] == 596)
solver.add(a1[3] + a1[11] + a1[12] + a1[9] + a1[13] - a1[0] - a1[2] - a1[7] - a1[14] - a1[16] == -78)

# Kiểm tra và in kết quả
if solver.check() == sat:
    model = solver.model()
    result = ''.join(chr(model[a].as_long()) for a in a1)
    print("Giá trị tìm thấy:", result)
else:
    print("No solution found")