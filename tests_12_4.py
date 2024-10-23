import rt_with_exceptions as rwe
import unittest
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run = rwe.Runner("Ivan", -5)
            for _ in range(10):
                    run.walk()
            self.assertEqual(run.distance, 40)
        except ValueError:(
            logging.warning(msg='Неверная скорость для Runner'))
        logging.info('Тест "test_walk" выполнен успешно')

    def test_run(self):
        try:
            run = rwe.Runner(777)
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
        logging.info('Тест "test_run" выполнен успешно')

    def test_challenge(self):
        run1 = rwe.Runner("Runner1")
        run2 = rwe.Runner("Runner2")
        for _ in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()