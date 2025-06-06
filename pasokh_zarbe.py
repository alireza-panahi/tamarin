name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
# -------------------------------------------------------------------
import numpy as np
from scipy.linalg import expm

class Matrice:
    def __init__(self, name):
        self.name = name
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        self.x0 = []
        self.ut = []

    def get_A(self):
        x = int(input('row A: '))
        for i in range(x):
            row = list(map(int, input('A row {} = '.format(i)).split()))
            self.A.append(row)
        self.A = np.array(self.A)  
        print('matrice A = \n{}'.format(self.A))
        return self.A

    def get_B(self):
        x = int(input('row B: '))
        for i in range(x):
            row = list(map(int, input('B row {} = '.format(i)).split()))
            self.B.append(row)
        self.B = np.array(self.B)  
        print('matrice B = \n{}'.format(self.B))
        return self.B

    def get_C(self):
        x = int(input('row C: '))
        for i in range(x):
            row = list(map(int, input('C row {} = '.format(i)).split()))
            self.C.append(row)
        self.C = np.array(self.C)
        print('matrice C = \n{}'.format(self.C))
        return self.C

    def get_D(self):
        x = int(input('row D: '))
        for i in range(x):
            row = list(map(int, input('D row {} = '.format(i)).split()))
            self.D.append(row)
        self.D = np.array(self.D)  
        print('matrice D = \n{}'.format(self.D))
        return self.D

    def get_x0(self):
        x = int(input('row x0: '))
        for i in range(x):
            row = list(map(int, input('x0 row {} = '.format(i)).split()))
            self.x0.append(row)
        self.x0 = np.array(self.x0)  
        print('matrice x0 = \n{}'.format(self.x0))
        return self.x0

    def get_ut(self):
        x = int(input('row ut: '))
        for i in range(x):
            row = list(map(int, input('ut row {} = '.format(i)).split()))
            self.ut.append(row)
        self.ut = np.array(self.ut)  
        print('matrice ut = \n{}'.format(self.ut))
        return self.ut

    def step_response(self, t):
    
        if len(self.A) == 0 or len(self.B) == 0 or len(self.C) == 0 or len(self.D) == 0 or len(self.x0) == 0:
            raise ValueError("تمامی ماتریس‌های A, B, C, D و x0 باید مقداردهی شوند.")

        A = np.array(self.A, dtype=float)
        B = np.array(self.B, dtype=float)
        C = np.array(self.C, dtype=float)
        D = np.array(self.D, dtype=float)
        x0 = np.array(self.x0, dtype=float)

        if A.shape[0] != A.shape[1]:
            raise ValueError("ماتریس A باید مربعی باشد.")
        if A.shape[0] != B.shape[0] or B.shape[1] != 1:
            raise ValueError("ابعاد ماتریس B نامناسب است.")
        if C.shape[0] != 1 or C.shape[1] != A.shape[0]:
            raise ValueError("ابعاد ماتریس C نامناسب است.")
        if D.shape != (1, 1):
            raise ValueError("ماتریس D باید 1x1 باشد.")
        if x0.shape != (A.shape[0], 1):
            raise ValueError("ابعاد بردار x0 نامناسب است.")

        u = np.ones((1, 1))

        y = []
        I = np.eye(A.shape[0])  
        for ti in t:
            eAt = expm(A * ti)
            A_inv = np.linalg.inv(A)
            x_t = eAt @ x0 + A_inv @ (eAt - I) @ B
            y_t = C @ x_t + D @ u
            y.append(y_t.flatten()[0])  

        return np.array(y)

if __name__ == "__main__":
    sys = Matrice("System")
    sys.get_A()  
    sys.get_B()  
    sys.get_C()  
    sys.get_D()  
    sys.get_x0() 

    t = np.linspace(0, 10, 100) 
    y = sys.step_response(t)
    print("پاسخ پله: \n", y)

    import matplotlib.pyplot as plt
    plt.plot(t, y, label="Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Output y(t)")
    plt.title("System Step Response")
    plt.grid(True)
    plt.legend()
    plt.show()