
# Programming with Induction
There are many great youtube tutorials on how to solve algorithmic problems. 

However, my goal in this repository (via videos) is to show that there is a different approach. An approach that: 
1. is systematic. 
2. shows how an algorithm designer thinks through the problem.

To do the first, we will rely ["on systematic thought, planning, and understanding from the very beginning, at every stage and for every step."](http://www.ccs.neu.edu/home/matthias/HtDP2e/part_preface.html)

To do the second, we will focus on how to break down a problem using the principle of mathematical induction. Mathematical induction shows up in many forms in programming from recursion to loop invariants. We will use induction to figure out how to break down a problem into smaller subproblems/subintances. The use of induction as our first tool in breaking down hard problems is [advocated by Udi Manber among others such as Edsger Dijkstra.]((https://www.amazon.com/Introduction-Algorithms-Creative-Udi-Manber/dp/0201120372/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1503354720&sr=8-1&keywords=udi+manber))     

My overarching goal is to show the user a "systematic way of thinking" that they can later apply to other algorithmic problems as well as general coding problems. 

The programming language we will use is Python as its syntax is accessible. 


## The Partition Problem

The first problem that we will study with this approach is The Partition Problem.

[YouTube playlist that plays the following videos in the correct order.](https://youtu.be/MXkYb-2MAoo?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 1: Introduction: Goals (2:03)](https://youtu.be/MXkYb-2MAoo?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 2: The Partition Problem (1:50)](https://youtu.be/_JogB4OQuJo?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 3: Applying Mathematical Induction (12:39)](https://youtu.be/eimW1y78WEE?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 4: Setting up tests for Partition Problem in Python (11:00)](https://youtu.be/G1PGLTD2xl4?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 5: The Partition Helper Function (13:47)](https://youtu.be/pyEZWvH7qPM?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 6: Type Comments for the Partition Problem (17:00)](https://youtu.be/Zu9T7eAyDWg?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 7: Writing the Partition Helper Function (4:51)](https://youtu.be/DOcL5eNn28Y?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 8: Type Table to Function (8:59)](https://youtu.be/OE77BhSf8XM?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

[Part 9: Dynamic Programming Approach (15:01)](https://youtu.be/UrV_PxL9KG0?list=PLw03yoxefBVGYFnLZO-saICoq1rT2oIBd)

Video lengths in parentheses (minutes). To align
with your level of comprehension, please feel free to adjust the
video to a faster speed.  


### Prerequisites

A basic understanding of the Principle of Mathematical Induction. A great introduction can be found [here.](https://youtu.be/KIHgHcIfq1Y)

A basic understanding of Python. 


### Code

The code to the Partiion Problem is included in this repository.

partitionProblem.py - goes through recursive approach to the Partition Problem

partitionProblemDP.py - is the Dynamic Programming approach to the problem

crossProductTable - contains the Cross Product Table of Type Comments as well as the Type Comments for Array and Target

## Authors

* Saumitra Saha

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments and Special Thanks

A sincere, special thanks to all the sources listed below. They changed the way I think about and write code. They trained me to have a principled way of thinking.

These two sources teach systematic development, data-driven programming and abstraction using Type Comments:


1. [How to Design Program(HtDP) by Felleinsen, Findler, Flatt, Krishnamurti](http://www.ccs.neu.edu/home/matthias/HtDP2e/part_preface.html)

2. Systematic Programming Design Course,by Gregor Kiczales, 
UBCx on Edx which has videos that teaches with HtDP. [Old version with video intro.](https://stage.edx.org/course/how-code-systematic-program-design-part-ubcx-spd1x#!)
[New version.](https://www.edx.org/course/how-code-simple-data-ubcx-htc1x) 


These two sources help you think about how to use induction to break down problems:

3. [How to Think about Algorithms by Jeff Edmonds](https://www.amazon.com/Think-About-Algorithms-Jeff-Edmonds-ebook/dp/B00AKE1SIE)
    (You can watch his [class videos on his homepage.](http://www.eecs.yorku.ca/~jeff/courses/3101/syllabus/) Shows how to think about hard ideas with abstract thinking with things like Fairy Godmothers!)


4. [Introduction to Algorithms: A Creative Approach by Udi Manber](https://www.amazon.com/Introduction-Algorithms-Creative-Udi-Manber/dp/0201120372/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1503354720&sr=8-1&keywords=udi+manber)
    (Forces you to see how an algorithm creator thinks with Induction. 
    [Chapter 5](https://github.com/haseebr/competitive-programming/blob/master/Materials/Introduction%20to%20Algorithms%20by%20Udi%20Manber.pdf) has some nice examples of using induction to creatively break down problems.)

Thanks to Geeks for Geeks for posting the problem, and code that I could cross reference:

5. GeeksforGeeks.org, [Partition Problem and Code.](http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/) 

6. Great explanation of pseudo-polynomial time, that should be the wikipedia post, [here.](https://stackoverflow.com/questions/19647658/what-is-pseudopolynomial-time-how-does-it-differ-from-polynomial-time)

Thanks to Bret Victor for posting his thoughts that influenced the way I see things:

7. Bret Victor on ["Up and Down the Ladder of Abstraction"](http://worrydream.com/#!2/LadderOfAbstraction) This is where the analogy of maps and walking in a new city that I use in these videos comes from.

8. Bret Victor on how teaching ["is about conveying a way of thinking"](http://worrydream.com/SomeThoughtsOnTeaching/)  