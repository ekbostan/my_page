from datetime import date
from django.shortcuts import render

all_posts =[
    {
        "slug":"Akb",
        "title": "Pong Player",
        "author_name": "LOLOLOLOLOLOL",
        "image":"ai.png",
        "content": "TensorFlow-based DQL(Deep Q-learning) player for the classic video game Pon.",
        "importance":"1",
        "github":"https://github.com/",
        "explanation": "LOLOLOLOLLLO"

    },
    {
        "slug":"ekb",
        "title": "Pong Player",
        "image": "pong.png",
        "content": "TensorFlow-based DQL(Deep Q-learning) player for the classic video game Pon.",
        "importance":"2",
        "github":"https://github.com/ekbostan/tensorflow-pong-cnn-playe",
        "explanation": "In my recent project, I had the opportunity to design and implement an AI-powered Ping-Pong player using advanced technologies such as Convolutional Neural Networks (CNNs) and Deep Q-Learning algorithms. To achieve optimal performance, I utilized several programming tools and languages such as Python with TensorFlow, Numpy, Matplotlib, OpenAI Gym, and Git.\n"+
            "The project required me to collect and preprocess large datasets of game frames and actions to train the CNNs and Deep Q-Learning models. With my efforts and dedication, I was able to achieve an impressive accuracy rate of 95%. I further optimized the neural network model's performance using a custom loss function and stochastic gradient descent (SGD) optimizer.\n"+
            "Throughout the project, I successfully managed the project timeline, demonstrating strong time management skills. As a final step, I wrote a comprehensive report that effectively communicated the project's objectives, methodology, results, and conclusions. I am proud to say that my logical thinking and creativity were instrumental in designing and implementing the AI-powered Ping-Pong player, and I look forward to working on similar projects in the future."
    },
    {
        "slug":"Ckb",
        "title": "AI-Connect4Player",
        "image": "connect4.png",
        "content":"AI player built using the minimax algorithm with alpha-beta pruning to play the classic game of Connect 4.",
        "importance":"3",
        "github":"https://github.com/ekbostan/AI-Connect4Player",
        "explanation": "I built an AI player in Python to play Connect 4. The player used the Minimax algorithm with Alpha-Beta Pruning optimization to make decisions. I utilized Python with NumPy, Pygame, Python Threading, and Git.To increase the chances of winning, I implemented the Minimax algorithm in Python to explore all possible moves, score each outcome, and select the optimal move. Additionally, I used Alpha-Beta Pruning to reduce the number of nodes evaluated in the search tree by pruning branches that cannot lead to a better move than the ones already explored.To optimize the algorithm's efficiency, I incorporated Alpha-Beta Pruning, which reduced the number of nodes evaluated in the search tree. I also developed a heuristic function to evaluate potential moves based on the number of possible winning combinations that could be achieved by placing a piece in a particular column.Overall, I demonstrated logical and critical thinking in designing and implementing the AI player and writing the report."
    },
     {
        "slug":"Dkb",
        "title": "Skamania II GPS",
        "image": "short_path.png",
        "content": "Using the A* algorithm with an admissible heuristic to find an optimal Path",
        "importance":"4",
        "github":"https://github.com/ekbostan/Shortest-Cost-Path-Python",
        "explanation": "The Skamania II GPS project aims to find the most hiker-friendly trail on a 3D terrain, represented by uniformly spaced tiles, using two cost functions to determine the cost of each move based on the change in height. To solve this problem, we propose using the A* algorithm with an admissible heuristic that can find the optimal path while being efficient.The A* algorithm is a popular pathfinding algorithm used in artificial intelligence that explores the search space while using a heuristic function to guide its search towards the goal node. To represent the terrain as a graph, each tile is considered as a node, and the weights of the edges are determined by the cost function used for each move. Once the graph is constructed, we can apply the A* algorithm to find the path with the lowest total cost.By applying this approach to real-world situations, hikers can find the most suitable trail based on their preferences and level of experience, making the hiking experience more enjoyable and safer."


     }
]

def get_priority(posts):
    return posts["importance"]

def home_page(request):
    sorted_projects = sorted(all_posts, key=get_priority)
    prioritized_projects = sorted_projects[-3:]
    return render(request,"new_blog/index.html",{
        "posts":prioritized_projects
    })

def about_me_page(request):
    return render(request,"new_blog/about.html")

def posts(request):
    return render(request,"new_blog/posts.html", {"posts":all_posts})

def post_info(request,slug):
    identified_project = next(post for post in all_posts if post['slug']== slug)
    return render(request,"new_blog/post_page.html",{"posts":identified_project})