<template>
    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
        <b-card>
            <div slot="header">
                <strong>Existing Pages</strong>
            </div>
            <b-row class="mt-3" v-for="page in existingPages" :key="page.pageType +'_' + page.id">
                <b-button block variant="outline-primary"
                          @click="$emit('change-visibility', page.pageType +'_' + page.id)">
                    {{page.page_name}}
                </b-button>
            </b-row>
            <b-row class="mt-3">
                <b-button block variant="outline-primary"
                          @click="$emit('change-visibility', 'new_form')">
                    Add New Page
                </b-button>
            </b-row>
        </b-card>
    </b-col>
</template>

<script>
    export default {
        name: 'edit-page-buttons',
        props: {
            existingPages: Array
        }
    }
</script>
