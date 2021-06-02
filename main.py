import os  #用于打开二维码图片
import qrcode #生成二维码
import options 


while True:

    print(' 1：加密信息\n 2：解密信息\n 3: 输入其他退出程序')
    action_str = input('请选择希望执行的操作: ')
    fn = 'result.png'

    if action_str == '1':
        key = '5c44c819appsapi0' #key已经确定
        data = input('输出你要加密的信息：')
        img = qrcode.make(options.aesEncrypt(key, data))
        img.save(fn)
        os.system(fn)
        

    elif action_str == '2':
        key = '5c44c819appsapi0' #同上
        data = input('请输入要解密的密文：')
        options.aesDecrypt(key, data)

    else:
        break

