from television_sim.model.controllers.controller import Controller
from television_sim.model.frames.frame import Frame
from television_sim.model.screens.screen import Screen


class Television:
    controller: Controller
    frame: Frame
    screen: Screen

    def set_frame(self, frame):
        self.frame = frame

    def set_screen(self, screen):
        self.screen = screen

    def set_controller(self, controller):
        self.controller = controller

    # Removendo a responsabilidade de ligar ou desligar de uma televisão
    # A responsabilidade de chamar os comandos é apenas do controlador

    # def turn_on(self):
    #     self.controller.turn_on()
    #
    # def turn_off(self):
    #     self.controller.turn_off()
