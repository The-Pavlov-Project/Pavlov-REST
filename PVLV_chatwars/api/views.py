from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from PVLV_chatwars.models import Game
from PVLV_games.models import GamePass
from .serializers import GamesSerializer, FullGamesSerializer


def get_game(game_pass, user_id):
    try:
        game_pass_obj = GamePass.objects.get(code=game_pass)
        game = Game.objects.get(game_pass=game_pass_obj.id, user=user_id)
        return game

    except GamePass.DoesNotExist:
        raise Exception({'message': 'game_pass does not exist'})
    except Game.DoesNotExist:
        raise Exception({'message': 'user_id does not exist'})


class GamesModelViewSet(ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GamesSerializer

    @action(detail=True, name='Get User', methods=['GET', 'PUT'])
    def game_pass(self, request, game_pass=None, user_id=None):

        try:
            game = get_game(game_pass, user_id)
        except Exception as exc:
            return Response(exc, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(FullGamesSerializer(game).data)

        elif request.method == 'PUT':
            serializer = FullGamesSerializer(game, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class TransferApiView(APIView):

    def get(self, request, game_pass=None, user_id=None):

        # user game obj
        try:
            user = get_game(game_pass, user_id)
        except Exception as exc:
            return Response(exc, status=HTTP_404_NOT_FOUND)

        try:
            amount = int(request.GET.get('amount', None))
        except ValueError as exc:
            return Response({'error': str(exc)}, status=HTTP_400_BAD_REQUEST)

        try:
            target_id = int(request.GET.get('target', None))
        except ValueError as exc:
            return Response({'error': str(exc)}, status=HTTP_400_BAD_REQUEST)

        # target game obj
        try:
            target = get_game(game_pass, target_id)
        except Exception as exc:
            return Response(exc, status=HTTP_404_NOT_FOUND)

        user.bits -= amount
        user.bits_given_away += amount

        target.bits += amount
        target.bits_received += amount

        user.save()
        target.save()
        return Response({'message': 'Transfered {} to {}'.format(amount, target.user.username)})


class PayApiView(APIView):

    def get(self, request, game_pass=None, user_id=None):

        try:
            user = get_game(game_pass, user_id)
            amount = int(request.GET.get('amount', None))
        except ValueError as exc:
            return Response({'error': str(exc)}, status=HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response(exc, status=HTTP_404_NOT_FOUND)

        user.bits -= amount
        user.save()
        return Response({'message': 'Payed {}'.format(amount)})