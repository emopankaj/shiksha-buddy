<template>
    <b-row class="align-items-center">
        <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
            <template v-for="(pages, pageType) in existingPages">
                <template v-for="currentPage in pages">
                    <edit-page-form :key="pageType +'_' + currentPage.id"
                                    :visible="visibleForm === pageType +'_' + currentPage.id"
                                    :page="{...currentPage, pageType : pageType}"/>
                </template>
            </template>
            <edit-page-form :visible="visibleForm === 'new_form'" :page="{
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
</template>

<script>
    import EditPageForm from "./EditPageForm";

    export default {
        name: 'edit-page-forms',
        components: {EditPageForm},
        props: {
            visibleForm: String,
            existingPages: Object,
        }
    }
</script>
