import numpy as np

def forward_pass(x1, x2, weight, bias):
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    net3 = x1 * weight['w13'] + x2 * weight['w23'] - bias['b3']
    out3 = sigmoid(net3)

    net4 = x1 * weight['w14'] + x2 * weight['w24'] - bias['b4']
    out4 = sigmoid(net4)

    net5 = out3 * weight['w35'] + out4 * weight['w45'] - bias['b5']
    out5 = sigmoid(net5)

    output = {'out3': out3, 'out4': out4, 'out5': out5}

    return output

def backward_pass(x1, x2, weight, bias, output, T, eta, a):
    def sigmoid_derivative(output):
        return output * (1 - output)
    
    out3, out4, out5 = output['out3'], output['out4'], output['out5']
    
    # 誤差梯度
    delta5 = sigmoid_derivative(out5) * (T - out5)

    delta3 = sigmoid_derivative(out3) * weight['w35'] * delta5

    delta4 = sigmoid_derivative(out4) * weight['w45'] * delta5

    # 更新偏置
    delta_b5 = - eta * delta5
    bias['b5'] += delta_b5

    delta_b3 = - eta * delta3
    bias['b3'] += delta_b3

    delta_b4 = - eta * delta4
    bias['b4'] += delta_b4

    # 更新權重
    delta_w35 = eta * out3 * delta5
    weight['w35'] += delta_w35

    delta_w45 = eta * out4 * delta5
    weight['w45'] += delta_w45

    delta_w13 = eta * x1 * delta3
    weight['w13'] += delta_w13

    delta_w14 = eta * x1 * delta4
    weight['w14'] += delta_w14

    delta_w23 = eta * x2 * delta3
    weight['w23'] += delta_w23

    delta_w24 = eta * x2 * delta4
    weight['w24'] += delta_w24

    return weight, bias

if __name__ == '__main__':
    x1 = 0.2
    x2 = 0.9
    weight = {
        'w13': 0.3, 'w14': 0.8,
        'w23': 0.4, 'w24': 0.6,
        'w35': 0.7, 'w45': 0.9
    }
    bias = {'b3': -1, 'b4': 1, 'b5': 1}
    T = 0.5
    eta = 5
    a = 0

    first_output = forward_pass(x1, x2, weight, bias)
    print(f"第一次輸出: {first_output['out5']}")

    weight, bias = backward_pass(x1, x2, weight, bias, first_output, T, eta, a)

    second_output = forward_pass(x1, x2, weight, bias)
    print(f"第二次輸出: {second_output['out5']}")