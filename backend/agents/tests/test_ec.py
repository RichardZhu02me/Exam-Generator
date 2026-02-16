from agents.agent import exam_compiler
from agents.core import ProblemState, ExamState
from langgraph.graph import StateGraph, START, END

problem_1 = {
    "problem": "### PMATH333 Real Analysis - Distinction-Level Problem\n\nConsider the ordered field of real numbers and let $x$ be in the set of real numbers such that $0 < x < 1$. Define a sequence $\\{a_n\\}$ by the recurrence relation:\n\n$$a_1 = x, \\quad a_{n+1} = 2a_n(1-a_n) + \\frac{1}{n}.$$\n\nPart A: Calculate $a_2$ and $a_3$ explicitly in terms of $x$.\n\nPart B: Show that if $\\lim_{n \\to \\infty} a_n = L$, then $0 \\leq L \\leq \\frac{1}{2}$.\n\nPart C: Determine whether $\\{a_n\\}$ is a Cauchy sequence, providing a rigorous justification based on the properties of ordered fields and the given recurrence relation.\n\n#### Twist:\n- You may not use a calculator or software to determine specific numerical values beyond variable expressions.\n- You must use the binomial theorem in your reasoning for Part B, considering that each $a_n$ can be expressed using combinations due to the recurrence formula's structure.",
    "solution": "**Solution:**\n\n**Part A:**\n- We start with $a_1 = x$.\n- For $a_2$, use the recurrence relation:\n\n  $$a_2 = 2a_1(1-a_1) + \\frac{1}{1} = 2x(1-x) + 1.$$\n\n- For $a_3$, apply the relation again:\n\n  $$a_3 = 2a_2(1-a_2) + \\frac{1}{2}.$$\n  \n  Substitute $a_2 = 2x(1-x) + 1$ into the formula for $a_3$ to express it in terms of $x$.\n\n**Part B:**\n- Assume $\\lim_{n \\to \\infty} a_n = L$. Then:\n  \n  $$L = 2L(1-L) + 0,$$\n  \n  simplifying gives $L = 2L - 2L^2$ or equivalently $0 = L - 2L^2$, implying $L(2L - 1) = 0$.\n\n- Therefore, $L = 0$ or $L = \\frac{1}{2}$.\n\n- In the interval $0 < a_n < 1$, use the binomial theorem to express $(1-a_n)^k$ for large $n$ and show that convergence forces $0 \\leq L \\leq \\frac{1}{2}$ through bounds defined by the series expansion.\n\n**Part C:**\n- The sequence $\\{a_n\\}$ is Cauchy:\n\n  Use the fact that $a_{n+1} = 2a_n(1-a_n) + \\frac{1}{n}$ to show despite $\\frac{1}{n}$, each $a_n$ brings close values as $n$ progresses, converging due to decreasing influence of $\\frac{1}{n}$.\n\n- State that based on the properties of recursive sequences and bounds, it ensures $|a_{n+1} - a_n| \\leq \\frac{2}{n}$, showing the diminishing difference making it Cauchy.",
    "rubric": "**Rubric:**\n\n- **Part A: (10 points)**\n  - 5 points for correctly finding $a_2$ in terms of $x$ using the recurrence relation.\n  - 5 points for applying the relation to determine $a_3$, showcasing understanding in handling recurrence relations.\n\n- **Part B: (15 points)**\n  - 10 points for clearly showing $L = 0$ or $L = \\frac{1}{2}$ using $L(2L - 1) = 0$.\n  - 5 points for incorporating the binomial theorem to explain convergence boundaries.\n\n- **Part C: (15 points)**\n  - 10 points for logical reasoning about the Cauchy property using the recurrence sequence and its diminishing property.\n  - 5 points for correctly arguing the $\\frac{1}{n}$ term's impact over large $n$, explaining convergence within the sequence.\n\nThe Trap:\n- Misusing limits or assuming direct factual infinities without demonstrating understanding of bounded impacts and convergence conditions will lead to mark deductions.",
}
problem_2 = {"problem": "problem", "solution": "some solution", "rubric": "a rubric"}
problems = ProblemState(problems=[problem_1, problem_2])

graph = StateGraph(ExamState, input_schema=ProblemState)
graph.add_node("Exam Compiler", exam_compiler)
graph.add_edge(START, "Exam Compiler")
graph.add_edge("Exam Compiler", END)
graph = graph.compile()

graph.invoke(problems)
