import asyncio
from python_mock_sandbox.mod1 import hello
from tests import async_return
from unittest.mock import MagicMock, PropertyMock, patch

from python_mock_sandbox import __version__
from python_mock_sandbox.app1 import main1, main1_async, main2, main2_async, main3


def test_version():
    assert __version__ == '0.1.0'

def test_main1():
    ''' 関数をモックする例

    ハマりどころ
      patchの第一引数に指定するimportのパスを間違えないように
        python_mock_sandbox.app1.hello <- o
        python_mock_sandbox.mod1.hello <- x
        python_mock_sandbox.app1.print <- o
        __main__.print                 <- x
    '''
    with patch('python_mock_sandbox.app1.hello', return_value='Dummy response') as hello_mock, \
         patch('python_mock_sandbox.app1.print') as print_mock:
        main1()
        hello_mock.assert_called_once_with('Kenshiro')
        print_mock.assert_called_once_with('Yo Dummy response')

def test_main1_async():
    ''' async関数をモックする例

    ハマりどころ
      async関数のモックですが、return_valueにFutureを指定しないようにすること
        return_value='Dummy response',               <- o
        return_value=async_return('Dummy response'), <- x
    '''
    with patch(
             'python_mock_sandbox.app1.hello_async',
             return_value='Dummy response',
         ) as hello_async_mock, \
         patch('python_mock_sandbox.app1.print') as print_mock:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main1_async())
            hello_async_mock.assert_called_once_with('Kenshiro')
            print_mock.assert_called_once_with('Yo Dummy response')

def test_main2():
    ''' クラスをモックする例

    ハマりどころ
    '''
    hello_obj_mock = MagicMock()
    hello_obj_mock.say.return_value = 'Dummy response'
    with patch('python_mock_sandbox.app1.Hello', return_value=hello_obj_mock), \
        patch('python_mock_sandbox.app1.print') as print_mock:
        main2()
        hello_obj_mock.say.assert_called_once_with('Kenshiro')
        print_mock.assert_called_once_with('Yo Dummy response')

def test_main2_async():
    ''' クラスの関数をモックする例

    ハマりどころ
      say_async関数の返り値にFutureを指定するように
        hello_obj_mock.say_async.return_value = async_return('Dummy response') <- o
        hello_obj_mock.say_async.return_value = 'Dummy response'               <- x
    '''
    hello_obj_mock = MagicMock()
    hello_obj_mock.say_async.return_value = async_return('Dummy response')
    with patch('python_mock_sandbox.app1.Hello', return_value=hello_obj_mock), \
        patch('python_mock_sandbox.app1.print') as print_mock:
        asyncio.run(main2_async())
        hello_obj_mock.say_async.assert_called_once_with('Kenshiro')
        print_mock.assert_called_once_with('Yo Dummy response')


def test_main3():
    ''' クラスのプロパティをモックする例

    ハマりどころ
      typeをつけるのを忘れずに
        type(hoge_obj_mock).i = hoge_obj_i_mock <- o
        hoge_obj_mock.i = hoge_obj_i_mock       <- x
      hoge_obj_mock.i.assert_called_once_with()はエラーになる
        hoge_obj_mock.i.assert_called_once_with() <- x
    '''
    hoge_obj_mock = MagicMock()
    hoge_obj_i_mock = PropertyMock(return_value=100)
    type(hoge_obj_mock).i = hoge_obj_i_mock
    with patch('python_mock_sandbox.app1.Hoge', return_value=hoge_obj_mock), \
        patch('python_mock_sandbox.app1.print') as print_mock:
        main3()
        hoge_obj_i_mock.assert_called_once_with()
        print_mock.assert_called_once_with('Hoge i=100')
