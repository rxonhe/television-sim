from television_sim.model.television.television import Television


class TelevisionBuilder:
    current_tv: Television

    def start_build(self):
        self.current_tv = Television()

    def throw_away(self):
        self.start_build()

    def add_frame(self, frame):
        self.current_tv.set_frame(frame)

    def add_screen(self, screen):
        self.current_tv.set_screen(screen)

    def add_controller(self, controller):
        self.current_tv.set_controller(controller)

    def get_tv(self):
        return self.current_tv
