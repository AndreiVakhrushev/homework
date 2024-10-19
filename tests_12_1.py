import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run =runner.Runner("Test Walker")
        for _ in range(10):
            run.walk()
        # Специально меняем на 40 (правильно 50)
        self.assertEqual(run.distance, 40)

    def test_run(self):
        run = runner.Runner("Test Runner")
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner("Runner1")
        run2 = runner.Runner("Runner2")
        # Вызываем у первого run, а у второго walk 10 раз
        for _ in range(10):
            run1.run()
            run2.walk()
        # Проверяем, что дистанции не равны (100 != 50)
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()

