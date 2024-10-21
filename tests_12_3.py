from homework.homework_module_12.homework_module_12_1 import runner
from homework.homework_module_12.homework_module_12_2 import runner_and_tournament as rat
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        run = runner.Runner("Test Walker")
        for _ in range(10):
            run.walk()
        # Специально меняем на 40 (правильно 50)
        self.assertEqual(run.distance, 40)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run = runner.Runner("Test Runner")
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        run1 = runner.Runner("Runner1")
        run2 = runner.Runner("Runner2")
        # Вызываем у первого run, а у второго walk 10 раз
        for _ in range(10):
            run1.run()
            run2.walk()
        # Проверяем, что дистанции не равны (100 != 50)
        self.assertNotEqual(run1.distance, run2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = rat.Runner('Усэйн', 10)
        self.runer_2 = rat.Runner('Андрей', 9)
        self.runer_3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn1(self):
        turn_1 = rat.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn2(self):
        turn_2 = rat.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn3(self):
        turn_3 = rat.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn4(self):
        turn_4 = rat.Tournament(4, self.runer_1, self.runer_2, self.runer_3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn4'] = result


if __name__ == '__main__':
    unittest.main()

