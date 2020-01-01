<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Add / Edit Pages</strong>
            </b-card-header>
            <b-card-body>
                <b-row class="align-items-center">

                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <template v-for="(pageType, index) in existingPages">
                            <template v-for="page in pageType">
                                <add-edit-page :id="index +'_' + page.id"
                                               :key="index +'_' + page.id"
                                               :button-label="page.page_name" :page="page"
                                               @change-visibility="visibleForm=$event"
                                               :visible-form="visibleForm"/>
                            </template>
                        </template>
                        <add-edit-page button-label="Add New Page" id="new_form" :page="{
                        id: '',
                        // FIXME: remove this
                        site_id: 'dummy',
                        pageType: 'TextImagePage',
                        page_name: '',
                        title: '',
                        heading: '',
                        text: '',
                        latitude: '-1',
                        longitude: '-1',
                        phone: '',
                        email: '',
                        facebook_link: '',
                        twitter_link: '',
                        address: ''
                    }"/>
                    </b-col>
                </b-row>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import AddEditPage from "./AddEditPage";
    import axios from "axios";

    export default {
        components: {AddEditPage},
        data() {
            return {
                existingPages: {},
                visibleForm: ''
            };
        },
        methods: {
            getAllPages() {
                axios.get('/api/page/')
                    .then(response => this.existingPages = response.data)
                    .catch(error => console.log(error))
            }
        },
        mounted() {
            this.getAllPages();
        }
    }
</script>