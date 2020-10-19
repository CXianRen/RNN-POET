# 基础RNN知识:https://zhuanlan.zhihu.com/p/85995376
# 工程base: https://pytorch.org/tutorials/beginner/chatbot_tutorial.html

# 如何使用
　一、使用已经训练好的模型
    python3 net.py 

        #　使用6000_checkpoint.tar 结果
        > 明月 酒  
        Bot: 明 月 生 明 夜 | 明 月 照 金 幡 | 不 识 春 来 事 | 空 寻 月 酒 时

        > 红花 江水
        Bot: 江 水 自 相 如 | 江 水 何 处 红 | 红 鱼 在 江 水 | 江 上 有 红 泥

        > 鲜奶
        Bot: 孤 生 自 有 趣 | 常 默 自 生 涯 | 何 以 问 斯 趣 | 人 生 无 限 情

　二、使用新的数据集
    需要修改preprocess_poet_jg_jueju.py的数据接口
    形成类似的格式的文件(如train_data/poet_jg_5jueju.txt)：
        xxx (输入字符串)　　        xxx(要输出的字符串)
        红妆 江梅 蛾眉 睡足	红妆夸睡足|粉额趁颜开|惟有江梅样|蛾眉淡拂来

    修改config　文件里的　poet_key_pait_path　为自定义数据集路径
　　 运行train.py

    修改net.py里main函数中　模型的载入路径(你刚刚训练好的保存路径)
    