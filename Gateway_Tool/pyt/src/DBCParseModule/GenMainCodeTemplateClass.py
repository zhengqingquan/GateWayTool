from abc import ABCMeta, abstractmethod


class GenMainCodeTemplateClass(metaclass=ABCMeta):

    @abstractmethod
    def Gen_DefinitionHeader(self):
        pass

    @abstractmethod
    def Gen_DefinitionSource(self):
        pass

    @abstractmethod
    def Gen_BinutilHeader(self):
        pass

    @abstractmethod
    def Gen_BinutilSource(self):
        pass

    @abstractmethod
    def Gen_MonitorutilHeader(self):
        pass

    @abstractmethod
    def Gen_MonitorutilSource(self):
        pass

    @abstractmethod
    def Gen_CycleActHeader(self):
        pass

    @abstractmethod
    def Gen_CycleActSource(self):
        pass

    @abstractmethod
    def Gen_ConfigHeader(self):
        pass

    @abstractmethod
    def Gen_MsgParseAOPHeader(self):
        pass

    @abstractmethod
    def Gen_MsgParseAOPSource(self):
        pass

    @abstractmethod
    def Gen_MsgCycAOPHeader(self):
        pass

    @abstractmethod
    def Gen_MsgCycAOPSource(self):
        pass

    def Gen_MainCode(self):
        self.Gen_DefinitionHeader()
        self.Gen_DefinitionSource()

        self.Gen_BinutilHeader()
        self.Gen_BinutilSource()

        self.Gen_MonitorutilHeader()
        self.Gen_MonitorutilSource()

        self.Gen_CycleActHeader()
        self.Gen_CycleActSource()

        self.Gen_ConfigHeader()

        self.Gen_MsgParseAOPHeader()
        self.Gen_MsgParseAOPSource()

        self.Gen_MsgCycAOPHeader()
        self.Gen_MsgCycAOPSource()
