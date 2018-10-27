# encoding:utf-8
###导入模块开始###
import tensorflow as tf
import numpy as np
import sys


def mlrun(BATCH_SIZE, SEED, learning_rate):
    # 写log
    class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "w")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass

    ###定义常量开始###
    # batch大小
    # 生成数据集的种子

    # 基于seed产生随机数
    rng = np.random.RandomState(SEED)
    # 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入的数据集
    X = rng.rand(32, 2)
    # 从X这个32行2列的矩阵中 取出一行 判断如果和小于1 给Y赋值1 如果和不小于1 给Y赋值0
    # 作为输出数据集的标签（正确答案）
    Y = [[int(x0 + x1 < 1)] for (x0, x1) in X]
    print("X:\n", X)
    print("Y:\n", Y)
    ###定义常量结束###

    ###前向传播开始###
    # 1定义神经网络的输入、参数和输出，定义前向传播过程。
    x = tf.placeholder(tf.float32, shape=(None, 2))
    y_ = tf.placeholder(tf.float32, shape=(None, 1))

    w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
    # 表示生成正态分布随机数，形状两行3列，标准差是2，均值为0，随机种子是1
    w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

    a = tf.matmul(x, w1)
    y = tf.matmul(a, w2)
    ###前向传播结束###

    ###反向传播开始###
    # 2定义损失函数和反向传播方法
    loss = tf.reduce_mean(tf.square(y - y_))
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
    ###反向传播结束###

    ###生成会话开始###
    # 3生成会话，训练STEPS轮
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        # 输出目前（未经训练）的参数取值。
        ###print(sess.run(w1))
        ###print(sess.run(w2))
        print("\n")
        # 训练模型。
        STEPS = 3000
        a=[]
        b=[]
        for i in range(STEPS):
            start = (i * BATCH_SIZE) % 32
            end = start + BATCH_SIZE
            sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
            if i % 200 == 0:
                total_loss = sess.run(loss, feed_dict={x: X, y_: Y})
                print("After %d training step(s),loss on all data is %g" % (i, total_loss))
                a.append(total_loss)
                b.append(i)
                c = dict(zip(b, a))
        # 输出训练后的参数取值
        #print(sess.run(w1))
        #print(sess.run(w2))
        return c
