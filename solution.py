import turtle
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
VEL = 5
BALL_MAX_VEL = 5
WINNING_SCORE = 3

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 10
SCORE_FONT = pygame.font.SysFont("comicsans", 40)


class Paddle:
    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color
        self.vel = vel

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self, direction):
        if direction == "up":
            self.y -= self.vel
        elif direction == "down":
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = random.choice([-5, -4, -3, 3, 4, 5])
        self.y_vel = random.randint(-2, 2)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)

    left_score_text = SCORE_FONT.render("Player1:  "+f"{left_score}", 1, YELLOW)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, PURPLE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, HEIGHT//10))
    win.blit(right_score_text, (WIDTH//4*3 - right_score_text.get_width()//2, HEIGHT//10))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 0:
            pygame.draw.rect(win, RED, (WIDTH//2 - 2, i, 4, 10))
    
    ball.draw(win)
    pygame.display.update()


def handle_collisions(ball, left_paddle, right_paddle):
    if ball.x - ball.radius <= left_paddle.x + left_paddle.width and left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
        ball.x_vel *= random.choice([-1.2, -0.9])
        middle_y = left_paddle.y + left_paddle.height//2
        difference = middle_y - ball.y
        reduction_factor = (left_paddle.height/2) / BALL_MAX_VEL
        ball.y_vel = difference / reduction_factor*-1
        left_paddle.color = random.choice([RED, BLUE, YELLOW, PURPLE])
    elif ball.x + ball.radius >= right_paddle.x and right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
        ball.x_vel *= random.choice([-1.2, -0.9])
        middle_y = right_paddle.y + right_paddle.height//2
        difference = middle_y - ball.y
        reduction_factor = (right_paddle.height/2) / BALL_MAX_VEL
        ball.y_vel = difference / reduction_factor*-1
        right_paddle.color = random.choice([RED, BLUE, YELLOW, PURPLE])

    elif ball.y - ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= random.choice([-1.2, -0.9])

    ball.color = random.choice([RED, BLUE, YELLOW, PURPLE])


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y >= left_paddle.vel:
        left_paddle.move("up")
    elif keys[pygame.K_s] and left_paddle.y <= HEIGHT - left_paddle.height - left_paddle.vel:
        left_paddle.move("down")

    if keys[pygame.K_UP] and right_paddle.y >= right_paddle.vel:
        right_paddle.move("up")
    elif keys[pygame.K_DOWN] and right_paddle.y <= HEIGHT - right_paddle.height - right_paddle.vel:
        right_paddle.move("down")


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE, VEL)
    right_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE, VEL)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, BLUE)
    left_score = 0
    right_score = 0
    won = False

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        if left_score == WINNING_SCORE:
            won = True
            win_text = SCORE_FONT.render("Player1 won!", 1, YELLOW)
        elif right_score == WINNING_SCORE:
            won = True
            win_text = SCORE_FONT.render("Player2 won!", 1, PURPLE)
        
        if won:
            WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//10))
            pygame.display.update()
            pygame.time.delay(3000)
            ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, BLUE)
            left_score = 0
            right_score = 0
            won = False

            

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collisions(ball, left_paddle, right_paddle)
        
        if ball.x - ball.radius <= 0:
            right_score += 1
            ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, BLUE)
        elif ball.x + ball.radius >= WIDTH:
            left_score += 1
            ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, BLUE)
        
    pygame.quit()


if __name__ == "__main__":
    main()


# # Create the game window
# window = turtle.Screen()
# window.title("Pong")
# window.bgcolor("black")
# window.setup(width=800, height=600)
# window.tracer(0)

# # Paddle A
# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.shapesize(stretch_wid=6, stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350, 0)

# # Paddle B
# paddle_b = turtle.Turtle()
# paddle_b.speed(0)
# paddle_b.shape("square")
# paddle_b.color("white")
# paddle_b.shapesize(stretch_wid=6, stretch_len=1)
# paddle_b.penup()
# paddle_b.goto(350, 0)

# # Ball
# ball = turtle.Turtle()
# ball.speed(240)
# ball.shape("square")
# ball.color("white")
# ball.penup()
# ball.goto(0, 0)
# ball.dx = 0.2
# ball.dy = -0.2

# # Functions to move the paddles
# def paddle_a_up():
#     y = paddle_a.ycor()
#     if y < 250:
#         y += 20
#     paddle_a.sety(y)

# def paddle_a_down():
#     y = paddle_a.ycor()
#     if y > -240:
#         y -= 20
#     paddle_a.sety(y)

# def paddle_b_up():
#     y = paddle_b.ycor()
#     if y < 250:
#         y += 20
#     paddle_b.sety(y)

# def paddle_b_down():
#     y = paddle_b.ycor()
#     if y > -240:
#         y -= 20
#     paddle_b.sety(y)

# # Keyboard bindings
# window.listen()
# window.onkeypress(paddle_a_up, "w")
# window.onkeypress(paddle_a_down, "s")
# window.onkeypress(paddle_b_up, "Up")
# window.onkeypress(paddle_b_down, "Down")

# # Main game loop
# while True:
#     window.update()

#     # Move the ball
#     ball.setx(ball.xcor() + ball.dx)
#     ball.sety(ball.ycor() + ball.dy)

#     # Border checking
#     if ball.ycor() > 290:
#         ball.sety(290)
#         ball.dy *= -1

#     if ball.ycor() < -290:
#         ball.sety(-290)
#         ball.dy *= -1

#     if ball.xcor() > 390:
#         ball.goto(0, 0)
#         ball.dx *= -1

#     if ball.xcor() < -390:
#         ball.goto(0, 0)
#         ball.dx *= -1

#     # Paddle and ball collisions
#     if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
#         ball.color("blue")
#         ball.setx(340)
#         ball.dx *= -1

#     if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
#         ball.color("red")
#         ball.setx(-340)
#         ball.dx *= -1
