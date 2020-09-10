import pygame

class BannerView:
    def __init__(self, screen, message, next, exit, score):
        self._banner(screen, message, next, exit, score)

    def _banner(self, screen, mode, next, exit, score):
        image = pygame.image.load(f"data/{mode}.png").convert()
        image_rect = image.get_rect().move(228, 258)
        screen.fill((0, 0, 0))
        screen.blit(image, image_rect)
        if score is not None:
            self._display_score(screen, score)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    return
                elif event.type == pygame.MOUSEBUTTONUP:
                    if image_rect.collidepoint(event.pos):
                        if not next():
                            return

    def _display_score(self, screen, score):
        lst = self._list_numbers(score)
        length = len(lst)
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        digits = [pygame.image.load(f"data/{s}.png").convert() for s in digits]
        x = 336 - 24*length//2
        y = 336
        for digit in lst:
            if digit == "-":
                image = digits[10]
            else:
                image = digits[digit]
            rect = image.get_rect().move(x, y)
            self._screen.blit(image, rect)
            x += 24

    def _list_numbers(self, num):
        neg = False
        if num < 0:
            neg = True
            num = -num
        lst = [num % 10]
        num = num // 10
        while num > 0:
            lst = [(num % 10)] + lst
            num = num // 10
        if neg:
            lst = ["-"] + lst
        return lst
