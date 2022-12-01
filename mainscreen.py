# class Mainscreen:
#
#     def welcome_main_screen:
#         """
#          Shows welcome images on the screen
#          """
#
#          p_x = int(screen_width / 5)
#         p_y = int((screen_height - game_image['player'].get_height()) / 2)
#         msgx = int((screen_width - game_image['message'].get_width()) / 2)
#         msgy = int(screen_height * 0.13)
#         b_x = 0
#         while True:
#         for event in pygame.event.get():
#         # if user clicks on cross button, close the game
#         if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
#         pygame.quit()
#         sys.exit()
#
#         # If the user presses space or up key, start the game for them
#         elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
#         return
#         else:
#         display_screen_window.blit(game_image['background'], (0, 0))
#         display_screen_window.blit(game_image['boy'], (p_x, p_y))
#         display_screen_window.blit(game_image['message'], (msgx, msgy))
#         display_screen_window.blit(game_image['base'], (b_x, play_ground))
#         pygame.display.update()
#         time_clock.tick(FPS)