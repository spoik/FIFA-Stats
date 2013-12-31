from django.shortcuts import render_to_response

from players.models import Player

def index(request):
	top_players = Player.top.all()
	bottom_players = Player.bottom.all()

	context = {
		"top_players": top_players,
		"bottom_players": bottom_players
	}

	return render_to_response("main/index.html", context)