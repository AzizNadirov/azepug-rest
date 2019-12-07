from django.utils import timezone

from rest_framework.test import APITestCase
from apps.base.views import get_models



class TestCreateModel(APITestCase):
    models = get_models()
    Profile = models['profile']


    def setUp(self):
        self.user_1 = self.Profile.objects.create_user(
            user_name = 'DonFeyzulla',
            email = 'fakeEmail@gm.com',
            password = "testing12345",
            first_name = 'Feyzulla')
        self.user_2 = self.Profile.objects.create_user(
            user_name = 'DonFeyzulla_2',
            email = 'fakeEmail_2@gm.com',
            password = "testing12345",
            first_name = 'Feyzulla')
        self.assertEqual(self.Profile.objects.all().count(), 2)

    def test_create_blog(self):
        Blog = self.models['blog']
        date_time = timezone.now()
        Blog.objects.create(title = 'test_title', content='test_content', author = self.user_1, date_created = date_time)
        self.assertEqual(Blog.objects.all().count(), 1)
        blog = Blog.published.get(id=1)
        self.assertEqual(blog.author, self.user_1)
        self.assertEqual(blog.title, 'test_title')
        self.assertEqual(blog.content, 'test_content')
        self.assertEqual(str(blog), f'<blog: test_title - {self.user_1}>')

    def test_create_employer_and_event(self):
        Employer = self.models['employer']
        employer = Employer.objects.create(added_by = self.user_1, name='emp name', founded_at = '1998-01-28')
        employer.workers.add(self.user_2)
        self.assertEqual(employer.workers.all().count(), 1)
        self.assertEqual(self.user_2 in employer.workers.all(), True)
        self.assertEqual(Employer.objects.all().count(), 1)
        self.assertEqual(str(employer), f'<employer: emp name - {self.user_1}>')

        Event = self.models['event']
        event = Event.objects.create(title = 'test_title', content='test_content', author = self.user_1,
                organiser = employer, starts_at = timezone.now(), ends_at = timezone.now())
        event.participants.add(self.user_2)
        self.assertEqual(self.user_2 in event.participants.all(), True)
        self.assertEqual(Event.objects.all().count(), 1)
        self.assertEqual(str(event), f'<event: test_title - {self.user_1}>')

    def test_create_news(self):
        News = self.models['news']
        date_time = timezone.now()
        News.objects.create(title = 'test_title', content='test_content', author = self.user_1, date_created = date_time)
        self.assertEqual(News.objects.all().count(), 1)
        news = News.published.get(id=1)
        self.assertEqual(news.author, self.user_1)
        self.assertEqual(news.title, 'test_title')
        self.assertEqual(news.content, 'test_content')
        self.assertEqual(str(news), f'<news: test_title - {self.user_1}>')

    def test_create_vacancy(self):
        Employer = self.models['employer']
        employer = Employer.objects.create(added_by = self.user_1, name='emp name', founded_at = '1998-01-28')
        Vacancy = self.models['vacancy']
        date = timezone.now().date()
        Vacancy.objects.create(
            author = self.user_1,
            title = 'test_title',
            content = 'test_content',
            employer = employer,
            dead_line = date,
            freelance = True,
            contact = 'test_contact',
            min_salary = 150
        )
        self.assertEqual(Vacancy.published.all().count(), 1)
        vacancy = Vacancy.published.get(id=1)
        self.assertEqual(vacancy.author, self.user_1)
        self.assertEqual(vacancy.title, 'test_title')
        self.assertEqual(vacancy.content, 'test_content')
        self.assertEqual(vacancy.employer, employer)
        self.assertEqual(vacancy.dead_line, date)
        self.assertEqual(vacancy.freelance, True)
        self.assertEqual(vacancy.contact, 'test_contact')
        self.assertEqual(vacancy.min_salary, 150)
        self.assertEqual(str(vacancy), f'<vacancy: test_title - {self.user_1}>')

    def test_create_question(self):
        Question = self.models['question']
        date_time = timezone.now()
        Question.objects.create(title = 'test_title', content='test_content', author = self.user_1, date_created = date_time)
        self.assertEqual(Question.objects.all().count(), 1)
        question = Question.published.get(id=1)
        self.assertEqual(question.author, self.user_1)
        self.assertEqual(question.title, 'test_title')
        self.assertEqual(question.content, 'test_content')
        self.assertEqual(str(question), f'test_title : {self.user_1.user_name}')

    def test_create_answer(self):
        Answer = self.models['answer']
        Question = self.models['question']
        date_time = timezone.now()
        Question.objects.create(title = 'test_title', content='test_content', author = self.user_1, date_created = date_time)
        self.assertEqual(Question.objects.all().count(), 1)
        question = Question.published.get(id=1)
        self.assertEqual(question.author, self.user_1)
        self.assertEqual(question.title, 'test_title')
        self.assertEqual(question.content, 'test_content')
        self.assertEqual(str(question), f'test_title : {self.user_1.user_name}')
  
        Answer.objects.create(content='test_content', author = self.user_1, 
                                date_created = date_time, question = question)
        self.assertEqual(Answer.objects.all().count(), 1)
        answer = Answer.published.get(id=1)
        self.assertEqual(answer.author, self.user_1)
        self.assertEqual(answer.content, 'test_content')
        self.assertEqual(answer.question, question)
        self.assertEqual(str(answer),  f"<answer: {self.user_1} to '{answer.question.title}'>")