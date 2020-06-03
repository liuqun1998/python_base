# 进程有自己的地址空间、内存
# 线程在一个进程下，共享同一片数据空间，包括开始、顺序、结束三个部分，一般采用并发

# 单核cpu不存在真正的并发
# 我们使用threading模块实现多线程代码


# 我们使用multiprocessing模块来实现多进程代码
# multiprocessing.Process创建进程
# start启动 join挂起
# os.getpid获得进程id
