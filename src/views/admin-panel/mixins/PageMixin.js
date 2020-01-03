import axios from "axios";

export default {
    methods: {
        getAllPages(callback) {
            axios.get('/api/page/')
                .then(response => callback(response.data))
                .catch(error => console.log(error))
        }
    }
}