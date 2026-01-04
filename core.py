def attach_powrush_divine(self):
    from .modules.powrush_divine import PowrushDivineModule
    self.powrush_module = PowrushDivineModule(self)
    print("Powrush Divine module attached — divine current ready.")
