from television_sim.configs.config import Config
from television_sim.model.controllers.controller_factory import ControllerFactory
from television_sim.model.frames.frame_factory import FrameFactory
from television_sim.model.screens.screen_factory import ScreenFactory
from television_sim.model.television.television_builder import TelevisionBuilder


def main():
    """Building TVs -- Orchestrator"""
    # Classe de configuração para instanciar comandos disponíveis
    config = Config()
    frame_factory = FrameFactory()
    screen_factory = ScreenFactory()
    # Os parâmetros commands utilizados pela factory de controllers não são mais instanciados ali dentro (D)
    controller_factory = ControllerFactory(config.commands)
    tvb = TelevisionBuilder()

    tvb.start_build()

    tvb.add_frame(frame_factory.build("samsung"))
    tvb.add_screen(screen_factory.build("lg"))
    tvb.add_controller(controller_factory.build("generic"))

    tv_0 = tvb.get_tv()

    # Removendo responsabilidade de television de chamar os comandos - (S)
    # tv_0.turn_on()
    # tv_0.turn_off()

    tv_0.controller.turn_on()
    tv_0.controller.turn_off()

    # criando segunda tv
    tvb.start_build()

    tvb.add_frame(frame_factory.build("samsung"))
    tvb.add_screen(screen_factory.build("lg"))
    # Criação de duas novas interfaces a partir de Controller(O) -> TimedOffController/TimedOnController (I)
    # Nova classe (SmartController extends TimedOffController) com funcionalidade de desligar com temporizador
    # Builder recebe ele (SmartController) sem perceber a mudança (Antes era Controller) (L)
    tvb.add_controller(controller_factory.build("smart"))

    tv_1 = tvb.get_tv()
    tv_1.controller.timed_off(2)


if __name__ == "__main__":
    main()
