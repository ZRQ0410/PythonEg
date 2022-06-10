class ImpactEffect:
    def impact(self):
        pass


class DamageEffect(ImpactEffect):
    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("伤害{}生命".format(self.value))


class CostSPEffect(ImpactEffect):
    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("消耗{}法力".format(self.value))


class LowerDefenceEffect(ImpactEffect):
    def __init__(self, value=0, time=0):
        self.value = value
        self.time = time

    def impact(self):
        super().impact()
        print("降低{}防御力{}秒".format(self.value, self.time))


class SkillBaseData:
    def __init__(self, name="", level=0):
        self.name = name
        self.level = level


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, base_data=None):
        self.base_data = base_data
        self.__config_file = self.__load_config_file()
        self.__effect_objects = self.__create_effect_objects()

    def __load_config_file(self):
        return {
            "降龙": ["DamageEffect(260)", "CostSPEffect(100)"],
            "六脉": ["DamageEffect(100)", "LowerDefenceEffect(0.7, 5)"],
        }

    def __create_effect_objects(self):
        effect_names = self.__config_file[self.base_data.name]
        # effect_objects = []
        # for i in effect_names:
        #     obj = eval(i)
        #     effect_objects.append(abj)
        # return effect_objects
        return [eval(i) for i in effect_names]

    def generate_skill(self):
        for i in self.__effect_objects:
            i.impact()


xl = SkillDeployer(SkillBaseData("降龙", 1))
xl.generate_skill()

lm = SkillDeployer(SkillBaseData("六脉", 1))
lm.generate_skill()
