import api from '@/api/api.service'

async function getUsers() {
    return api.get(`/users`)
        .then(response => response.data)
}

export default {
	getUsers
}