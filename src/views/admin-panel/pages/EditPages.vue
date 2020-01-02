<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Add / Edit Pages</strong>
            </b-card-header>
            <b-card-body>
                <edit-page-buttons :existing-pages="existingPages" @change-visibility="visibleForm=$event"/>
                <edit-page-forms :existing-pages="existingPages" :visible-form="visibleForm"
                                 @refresh-pages="refreshPages"/>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import axios from "axios";
    import {EventBus} from '@/main'
    import EditPageForms from "./EditPageForms";
    import EditPageButtons from "./EditPageButtons";

    export default {
        components: {EditPageForms, EditPageButtons},
        data() {
            return {
                existingPages: {},
                visibleForm: ''
            };
        },
        methods: {
            refreshPages() {
                axios.get('/api/page/')
                    .then(response => this.existingPages = response.data)
                    .catch(error => console.log(error))
            }
        },
        mounted() {
            this.refreshPages();
            EventBus.$on('refresh-pages', this.refreshPages);
        }
    }
</script>