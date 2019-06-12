import HTMLReport  # 导入HTMLReport展示测试结果
import unittest  # 导入unittest
import requests  # 导入requests库
import json  # 导入json


class LianXi(unittest.TestCase):  # 定义一个类，类的首字母要大写哦
    def setUp(self):  # 初始化
        print('初始化环境')

    def tearDown(self):
        print('清理环境结束')

    def test_get_success(self):  # 定义一个方法，切记要以test开头哦
        self.base_url = 'http://tradesearch.intra.uat.beyonds.gw/order/v1/queryOrderDetail?'
        datalist = {'orderNo': '1124525633475153920'}  # 定义传参数据
        head = {"Content-Type": "application/Json"}  # 定义头部
        r = requests.get(self.base_url, params=datalist, headers=head)  # 传入参数
        result = json.loads(r.text)  # 使用json格式返回
        self.assertEqual(result['status'], 200)  # 检验返回值

    # print(result)

    # @unittest.skip('跳过了')
    def test_post(self):
        params = {'memberId': 17000001000000090, 'orderNo': 1125907915276521472}
        base_url = 'http://trade.intra.uat.beyonds.gw/order/v1/orderComplete?'
        r = requests.post(url=base_url, params=params)
        r = json.loads(r.text)
        self.assertEqual(r['status'], 200)
        # print(result)

    def test_get1(self):
        base_url = 'http://xmtm.intra.sit.beyonds.gw/v1/template/getPlazaList/T0097719855944359936'
        r = requests.get(base_url)
        r = json.loads(r.text)
        self.assertEqual(r['status'], 200)
        # print(requests)


if __name__ == '__main__':
    """
    unittest执行过程：
                    1.新建测试类且继承于：unittest.TestCase
                    2.重写setUp()初始化函数和tearDown()清理/拆解函数
                    3.以test开头定义测试函数
                    4.用装饰器@unittest.skip()跳过测试用例
                    5.在程序入口if __name__ == '__main__'：中实例化测试套件： suite = unittest.TestSuite()
                    6.实例化测试套件加载器：loader = unittest.TestLoader()
                    7.测试套件对象suite调用addTests()方法,将测试用例加载器对象loader调用loadTestFromTestCase(测试类名)获取的用例添加到测试用例中
                    8.调用HTMLReport.TestRunner()方法实例化测试用例执行器runner
                    9.测试用例执行器runner调用run()方法执行测试套件suite并生成报告


    """

    # 测试套件
    suite = unittest.TestSuite()
    # 测试用例加载器
    loader = unittest.TestLoader()
    # 把测试用例加载到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(LianXi))

    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path=r'C:\Users\Qianyue\Desktop\report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    # 执行测试用例套件
    runner.run(suite)


