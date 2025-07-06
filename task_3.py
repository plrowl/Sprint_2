class PointsForPlace:
    @staticmethod
    def get_points_for_place(place: int):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, place, meters):
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        total = points_place + points_meters
        return total