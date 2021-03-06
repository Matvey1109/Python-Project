from django.shortcuts import render, redirect
from .models import Contact, ContactPermissions


def contacts(request):
    search_input = request.GET.get('search_area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        search_input = ''
        cp = ContactPermissions.objects.filter(author=request.user)
        contacts = Contact.objects.none()
        for c in cp:
            contacts |= Contact.objects.filter(author=c.whom)
    return render(request, 'contacts/contacts.html', {'contacts': contacts, 'search_input': search_input})


def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST['full_name'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            address=request.POST['address']
        )
        new_contact.author = request.user
        new_contact.save()
        ContactPermissions.objects.create(author=request.user, whom=request.user)
        return redirect('/contacts/')
    return render(request, 'contacts/add_contact.html')


def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/contact_profile.html', {'contact': contact})


def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['full_name']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone_number']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/contacts/contact_profile/' + str(contact.id))
    return render(request, 'contacts/edit_contact.html', {'contact': contact})


def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/contacts/')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})