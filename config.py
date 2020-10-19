
#数据预处理
search_path=r'./jg_data/Datasets/CCPC/*.json'
poet_output_path='./train_data/poet_tang_jg_5jueju.json'
poet_key_pait_path='./train_data/poet_jg_5jueju.txt'

# Default word tokens
PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token

#网络参数
MAX_LENGTH = 25   # 输出的最大长度
MIN_COUNT  = 3    #最小输入长度

# Configure models
model_name = 'lhei_model'
attn_model = 'dot'
#attn_model = 'general'
#attn_model = 'concat'
hidden_size = 500
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1

embedding_size=5835 　　　　#运行 VOC.py 会输出对应的尺寸

#训练参数
save_dir ="./save"
batch_size = 128            　　#根据GPU资源修改这里
clip = 50.0
teacher_forcing_ratio = 1.0
learning_rate = 0.0001     #
decoder_learning_ratio = 5.0
n_iteration = 10000         #　修改这里修改训练次数
print_every = 10            #　log输出间隔
save_every = 3000        　 #　 模型保存间隔
checkpoint_iter = 1000