u = User.userManager.get(id=request.session['user']['id'])
        u.save()
        trip = Trip.tripManager.create(destination=request.POST['destination'], description=request.POST['description'], start_date = request.POST['start_date'], end_date = request.POST['end_date'])
        trip.save()
        trip.users.add(u)
        trip.save()
        id = User.userManager.get(id=request.session['user']['id'])