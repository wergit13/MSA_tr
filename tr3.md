$$n=18; i=15$$

**Задача 1.** Пусть $\xi \sim B(1,\theta)$ - биномиальная случайная величина с вероятностью успеха в одном опыте - $\theta$. Возможные значения параметра $\theta_1=0,3+(\frac{i}{10n})$, $\theta_2=0,5+(\frac{i}{10n}) $. Множество решений состоит из двух элементов $D=\{d_1, d_2 \}$. Функция потерь $L$ имеет вид 
|          | $d_1$ | $d_2$ |
|:--------:|:-----:|:-----:|
|$\theta_1$| $0$   | $2+(\frac{i}{n})$   |
|$\theta_2$|  $3+(\frac{1,5 \cdot i}{n})$  | $1+(\frac{0,5 \cdot i}{n})$   |

**Найти:**
---  
**а.**  Оптимальную минимаксную решающую  $\delta^*(x)$

$\xi \sim B(1,\theta)$

$X = \{0, 1\}$ - множество возможных исходов

$\theta_1=0,3+(\frac{15}{10 \cdot 18})= \frac{23}{60} $

$\theta_2=0,5+(\frac{15}{10 \cdot 18}) = \frac{7}{12}  $

Функция потерь $L$ имеет вид 
|          | $d_1$ | $d_2$ |
|:--------:|:-----:|:-----:|
|$\theta_1$| $0$   | $2 + \frac{15}{18} = \frac{17}{6}$   |
|$\theta_2$|  $3+\frac{1,5 \cdot 15}{18} = \frac{17}{4}$  | $1 + \frac{0,5 \cdot 15}{18} = \frac{17}{12}$   |

Возможные решающие функции

$\delta_1 = d_1, x=\{0, 1\} $

$\delta_2 = d_2, x=\{0, 1\} $

$\delta_3 = \{d_1, x=0;\quad d_2, x=1 \}$

$\delta_4 = \{d_1, x=1;\quad d_2, x=0 \}$

Функция риска

$R(\theta_i, \delta_j) = ML\big(\theta_i, \delta_j(\xi)\big) = P(\xi=0 | \theta_i) \cdot L\big(\theta_i, \delta_j(0)\big) \quad + \quad P(\xi=1 | \theta_i) \cdot L\big(\theta_i, \delta_j(1)\big) $

Рассчитаем функции риска для каждой $\delta_j$ с возможными $\theta_i$

$R(\theta_1, \delta_1) = ML(\theta_1, \delta_1) =  \frac{23}{60} \cdot L(\theta_1, \delta_1(1)) + \frac{37}{60} \cdot L(\theta_1, \delta_1(0)) = \frac{23}{60} \cdot 0 + \frac{37}{60} \cdot 0 = 0$

$R(\theta_2, \delta_1) = ML(\theta_2, \delta_1) =  \frac{7}{12} \cdot L(\theta_2, \delta_1(1)) + \frac{5}{12} \cdot L(\theta_2, \delta_1(0)) = \frac{7}{12} \cdot \frac{17}{4} + \frac{5}{12} \cdot \frac{17}{4} = \frac{17}{4} = 4.25$

$R(\theta_1, \delta_2) = ML(\theta_1, \delta_2) =  \frac{23}{60} \cdot L(\theta_1, \delta_2(1)) + \frac{37}{60} \cdot L(\theta_1, \delta_2(0)) = \frac{23}{60} \cdot \frac{17}{6} + \frac{37}{60} \cdot \frac{17}{6} = 2.83$

$R(\theta_2, \delta_2) = ML(\theta_2, \delta_2) =  \frac{7}{12} \cdot L(\theta_2, \delta_2(1)) + \frac{5}{12} \cdot L(\theta_2, \delta_2(0)) = \frac{7}{12} \cdot \frac{17}{12} + \frac{5}{12} \cdot \frac{17}{12} = \frac{17}{12} = 1.417$

$R(\theta_1, \delta_3) = ML(\theta_1, \delta_3) =  \frac{23}{60} \cdot L(\theta_1, \delta_3(1)) + \frac{37}{60} \cdot L(\theta_1, \delta_3(0)) = \frac{23}{60} \cdot \frac{17}{6} + \frac{37}{60} \cdot 0 = 1.0861$

$R(\theta_2, \delta_3) = ML(\theta_2, \delta_3) =  \frac{7}{12} \cdot L(\theta_2, \delta_3(1)) + \frac{5}{12} \cdot L(\theta_2, \delta_3(0)) = \frac{7}{12} \cdot \frac{17}{12} + \frac{5}{12} \cdot \frac{17}{4} = 2.597$

$R(\theta_1, \delta_4) = ML(\theta_1, \delta_4) =  \frac{23}{60} \cdot L(\theta_1, \delta_4(1)) + \frac{37}{60} \cdot L(\theta_1, \delta_4(0)) = \frac{23}{60} \cdot 0 + \frac{37}{60} \cdot \frac{17}{6} = 1.747$

$R(\theta_2, \delta_4) = ML(\theta_2, \delta_4) =  \frac{7}{12} \cdot L(\theta_2, \delta_4(1)) + \frac{5}{12} \cdot L(\theta_2, \delta_4(0)) = \frac{7}{12} \cdot \frac{17}{4} + \frac{5}{12} \cdot \frac{17}{12} = 3.069$

Найдем максимальное значение функции потерь для каждой $\delta_j$

$R(\theta_i, \delta_1) = 4.25$

$R(\theta_i, \delta_2) = 2.83$

$R(\theta_i, \delta_3) = 2.597$

$R(\theta_i, \delta_4) = 3.069$

По принципу минимакса $\delta_3$ - оптимальная минимаксная решающая функция

*Ответ:* $\delta^*(x) = \delta_3$

---

**б.** Пусть имеет априорное распределение $\pi(\theta_1) = \beta, \pi(\theta_1) = (1 - \beta), \quad 0< \beta < 1 $. Найти оптимальное байесовское решение $\delta^*(x)$ и байесовский риск $r(\delta^*)$.  Построить график в зависимости от $\beta$.

Найдем полные вероятности появления возможных $\xi$

$P(\xi=0) = \pi(\theta_1) \cdot P(\xi=0| \theta_1) + \pi(\theta_2) \cdot P(\xi=0| \theta_2) = \beta \cdot (1-\theta_1) +  (1-\beta) \cdot (1-\theta_2) = \frac{37}{60}\beta + \frac{5}{12} - \frac{5}{12}\beta =  \frac{5}{12}  + \frac{1}{5}\beta$

$P(\xi=1) = 1 - P(\xi=0) = 1 - ( \frac{5}{12} + \frac{1}{5}\beta )=  \frac{7}{12} - \frac{1}{5}\beta$

Вычислим условные вероятности параметра $\theta$ при $\xi=x; x = \{0, 1\}$

$P(\theta=\theta_1|\xi=1) = \frac{\pi(\theta_1)P(\xi=1|\theta_1)}{P(\xi=1)} = \frac{\frac{23}{60}\beta}{\frac{7}{12} - \frac{1}{5}\beta} = \frac{23\beta}{35-12\beta}$

$ P(\theta=\theta_2|\xi=1) = 1 - P(\theta=\theta_1|\xi=1) = 1 -  \frac{23\beta}{35-12\beta} = \frac{35(1- \beta)}{35-12\beta}$

$P(\theta=\theta_1|\xi=0) = \frac{\pi(\theta_1)P(\xi=0|\theta_1)}{P(\xi=0)} = \frac{\frac{37}{60}\beta}{\frac{5}{12}  + \frac{1}{5}\beta} = \frac{37\beta}{25+12\beta}$

$P(\theta=\theta_2|\xi=0) = 1 - P(\theta=\theta_1|\xi=0) = 1 - \frac{37\beta}{25+12\beta} = \frac{25(1- \beta)}{25+12\beta} $

Найдем оптимальное решение.

Срение потери по условыным распределения $\beta$

$ML(\theta | \xi=0, d=d_1) = P(\theta_1| \xi=0)L(\theta_1, d_1) + P(\theta_2| \xi=0)L(\theta_2, d_1) = \frac{37\beta}{25+12\beta} \cdot 0 + \frac{25(1- \beta)}{25+12\beta} \cdot \frac{17}{4} = \frac{425(1-\beta)}{100+48\beta} $ 

$ML(\theta | \xi=0, d=d_2) = P(\theta_1| \xi=0)L(\theta_1, d_2) + P(\theta_2| \xi=0)L(\theta_2, d_2) = \frac{37\beta}{25+12\beta} \cdot \frac{17}{6} + \frac{25(1- \beta)}{25+12\beta} \cdot \frac{17}{12} = \frac{833\beta+425}{300+144\beta} $ 

$ML(\theta | \xi=1, d=d_1) = P(\theta_1| \xi=1)L(\theta_1, d_1) + P(\theta_2| \xi=1)L(\theta_2, d_1) = \frac{23\beta}{35-12\beta} \cdot 0 + \frac{35(1- \beta)}{35-12\beta} \cdot \frac{17}{4} = \frac{595(1-\beta)}{140-48\beta} $ 

$ML(\theta | \xi=1, d=d_2) = P(\theta_1| \xi=1)L(\theta_1, d_2) + P(\theta_2| \xi=1)L(\theta_2, d_2) = \frac{23\beta}{35-12\beta} \cdot \frac{17}{6} + \frac{35(1- \beta)}{35-12\beta} \cdot \frac{17}{12} = \frac{187\beta - 595}{420 - 144\beta} $

Найдем точку пересечения: $ \frac{425(1-\beta)}{100+48\beta} = \frac{833\beta+425}{300+144\beta} $; $\beta = \frac{25}{62} \approx 0.4$ 