import course

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='Chemistry',
                  teacher_name='Mr. Ng',
                  resource_name='Mole Conversions',
                  resource_url='http://www.kentchemistry.com/links/GasLaws/moleconversions.htm'),
    course.Course(period=3,
                  name='Algebra 2',
                  teacher_name='Mr. Shelton',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/algebra2'),
    course.Course(period=4,
                  name='C Aide',
                  teacher_name='Mr. Skold',
                  resource_name='Schooloop',
                  resource_url='https://ssfhs.schoolloop.com/portal/login?redirect=i22tb1u9ovvs'),
    course.Course(period=5,
                  name='English 3CP',
                  teacher_name='Ms. Marder',
                  resource_name='Sparknotes',
                  resource_url='http://www.sparknotes.com/'),
    course.Course(period=6,
                  name='US History',
                  teacher_name='Mr. Killeen',
                  resource_name='National History Day',
                  resource_url='https://nhd.org/'),
]