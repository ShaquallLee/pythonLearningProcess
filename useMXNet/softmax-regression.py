import d2lzh as d2l
from mxnet import gluon, init, autograd
from mxnet.gluon import loss as gloss, nn
import sys
import time

def get_fashion_mnist_labels(labels):
    '''
    将数据包中的数值标签转成相应的文本标签
    :param labels:
    :return:
    '''
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

def show_fashion_mnist(images, labels):
    '''
    在一行中画出多张图像和对应标签的函数
    :param images:
    :param labels:
    :return:
    '''
    d2l.use_svg_display()
    _, figs = d2l.plt.subplots(1, len(images), figsize=(12, 12))
    for f, img, lbl in zip(figs, images, labels):
        f.imshow(img.reshape((28, 28)).asnumpy())
        f.set_title(lbl)
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)


def train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,params=None, lr=None, trainer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            with autograd.record():
                y_hat = net(X)
                l = loss(y_hat, y).sum()
            l.backward()
            if trainer is None:
                d2l.sgd(params, lr, batch_size)
            else:
                trainer.step(batch_size) # “softmax回归的简洁实现”
            y = y.astype('float32')
        train_l_sum += l.asscalar()
        train_acc_sum += (y_hat.argmax(axis=1) == y).sum().asscalar()
        n += y.size
        test_acc = d2l.evaluate_accuracy(test_iter, net)
        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f' % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))


if __name__ == '__main__':
    batch_size = 256
    train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

    net = nn.Sequential() #sequential用来存储所有神经网络中的所有单元
    net.add(nn.Dense(10)) #设置网络输出个数为10
    net.initialize(init.Normal(sigma=0.01)) #初始化网络参数为从均值为0、标准差为0.01的正态分布的随机取样的值

    loss = gloss.SoftmaxCrossEntropyLoss() # softmax运算和交叉熵损失计算的函数

    trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1}) # 使⽤学习率为0.1的小批量随机梯度下降作为优化算法
    num_epochs = 10
    d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs,
                  batch_size, None, None, trainer) #训练并输出结果
    for X, y in test_iter:
        break
    true_labels = d2l.get_fashion_mnist_labels(y.asnumpy())
    pred_labels = d2l.get_fashion_mnist_labels(net(X).argmax(axis=1).asnumpy())
    print(true_labels)
    print(pred_labels)
    print(float(len([x for x in range(len(true_labels)) if true_labels[x] == pred_labels[x]]))/len(true_labels))
