from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.response import Response

from . c4methods.c4functions import *
from . c4methods.minimax_util import minimax_decision, alpha_beta_search

class UpdateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            board = request.data.get('board')
            currPlayer = request.data.get('currPlayer')
            oppPlayer = request.data.get('oppPlayer')
            winner = get_winner(board)
            gameOver = winner is not None


            return Response({
                'board': board,
                'currPlayer': currPlayer,
                'oppPlayer': oppPlayer,
                'gameOver': gameOver,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MinmaxResponse(APIView): 
    def post(self, request, *args, **kwargs):
        try:
            board = request.data.get('board')
            currPlayer = request.data.get('currPlayer')
            
            action = alpha_beta_search(board, currPlayer, 6)

            return Response({
                'action': action
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
