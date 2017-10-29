from tkinter import *
class Pong(Frame):
    def createWidgets(self):
        ## 画布
        self.draw = Canvas(self, width="5i", height="5i", bg='white')

        ## 游标(控制小球移动速度，范围：[-100, 100])
        self.speed = Scale(self, orient=HORIZONTAL, label="ball speed",
                           from_=-100, to=100)

        self.speed.pack(side=BOTTOM, fill=X)

        #小球碰撞墙壁的范围
        self.scaling_right = 4.8
        self.scaling_left = 0.2
        #小球直径
        self.ball_d = 0.4
        #游标度数
        self.scale_value = self.speed.get()
        #放缩率
        self.scaling = 100.0

        #存放小球数组
        self.balls = []
        #存放小球x坐标数组
        self.ball_x = []
        #存放小球y坐标数组
        self.ball_y = []
        #存放小球x轴方向速度数组
        self.ball_v_x = []
        #存放小球y轴方向速度数组
        self.ball_v_y = []

        # 一个小球
        self.ball = self.draw.create_oval("0.10i", "0.10i", "0.50i", "0.50i",
                                          fill="red")
                #把五个小球放入数组
        self.balls.append(self.ball)
        #第一个小球，即self.ball的圆心坐标(self.x, self.y),这里进行了放缩,目的是为了
        #在小球移动的过程中更加流畅
        self.x = 0.3        
        self.y = 0.3
        #第一个小球的速度方向
        self.velocity_x = -0.2
        self.velocity_y = 0.5

        self.second_ball_x = 0.9
        self.second_ball_y = 0.9
        self.second_ball_v_x = 0.4
        self.second_ball_v_y = -0.5

        self.three_ball_x = 1.5
        self.three_ball_y = 1.5
        self.three_ball_v_x = -0.3
        self.three_ball_v_y = -0.5

        self.four_ball_x = 2.2
        self.four_ball_y = 2.2
        self.four_ball_v_x = 0.1
        self.four_ball_v_y = -0.5

        self.five_ball_x = 3.2
        self.five_ball_y = 3.2
        self.five_ball_v_x = 0.3
        self.five_ball_v_y = 0.5

        
        #更新小球的坐标
        self.update_ball_x_y()
        self.draw.pack(side=LEFT)

    def update_ball_x_y(self, *args):
        #第一个小球信息
        self.ball_x.append(self.x)
        self.ball_y.append(self.y)
        self.ball_v_x.append(self.velocity_x)
        self.ball_v_y.append(self.velocity_y)
    def update_ball_velocity(self, index, *args):
        #游标值
        self.scale_value = self.speed.get()
        #碰撞墙壁
        if (self.ball_x[index] > self.scaling_right) or (self.ball_x[index] < self.scaling_left):
            self.ball_v_x[index] = -1.0 * self.ball_v_x[index]
        if (self.ball_y[index] > self.scaling_right) or (self.ball_y[index] < self.scaling_left):
            self.ball_v_y[index] = -1.0 *  self.ball_v_y[index]
        for n in range(len(self.balls)):
            #小球碰撞条件，即：(x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
            if (round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2)):
                #两小球速度交换
                temp_vx = self.ball_v_x[index]
                temp_vy = self.ball_v_y[index]
                self.ball_v_x[index] = self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[n]
                self.ball_v_x[n] = temp_vx
                self.ball_v_y[n] = temp_vy
        #print(self.ball_v_x, self.ball_v_y)
    def get_ball_deltax(self, index, *args):
        '''获取小球X轴坐标移动距离并且更新小球的圆心X坐标，返回X轴所需移动距离'''
        deltax = (self.ball_v_x[index] * self.scale_value / self.scaling)
        self.ball_x[index] = self.ball_x[index] + deltax
        return deltax

    def get_ball_deltay(self, index, *args):
        '''获取小球Y轴坐标移动距离并且更新小球的圆心Y坐标，返回Y轴所需移动距离'''
        deltay = (self.ball_v_y[index] * self.scale_value / self.scaling)
        self.ball_y[index] = self.ball_y[index] + deltay
        return deltay
    
    def moveBall(self, *args):
        '''移动第一个小球，编号为：0,这是根据数组：self.balls确定的。'''
        self.update_ball_velocity(0)       
        deltax = self.get_ball_deltax(0)
        deltay = self.get_ball_deltay(0)
        #小球移动
        self.draw.move(self.ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.moveBall)
        
    def __init__(self, master=None):
        '''初始化函数'''
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.moveBall)
        
game = Pong()

game.mainloop()
