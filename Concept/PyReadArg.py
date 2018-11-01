    """
    第一种方式可以在命令行随意输入参数，
    第二种方式在python Test1.py后，输入的参在数必须是在代码里面添加了的，而且格式必须为--args，写成sys也会报错
    第三种方式，源于对第二种方式的封装，但是可以在命令行输入代码里没有参数，反正代码里没有定义，也不会对程序有影响，定义的方式可以写成--args, 也可以写成-args(单个减号)
    """
    # 第一种方式 sys
    import sys 
    path_dir = sys.argv[0]
    arg_test = sys.argv[1]
    print(sys.argv[0])
    print(sys.argv[1])


    # 第二种方式 argparse
    import argparse
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--gpus', type=str, default = "None")
    parser.add_argument('--batch-size', type=int, default=32)
    args = parser.parse_args()
    print(args.gpus)
    print(args.batch_size)
    print(args)

    # 第三种方式 tf
    import tensorflow as tf
    tf.app.flags.DEFINE_string('gpus', None, 'gpus to use')
    tf.app.flags.DEFINE_integer('batch_size', 5, 'batch size')
    FLAGS = tf.app.flags.FLAGS

    def main(_):
        print(FLAGS.gpus)
        print(FLAGS.batch_size)

    if __name__=="__main__":
        tf.app.run()
