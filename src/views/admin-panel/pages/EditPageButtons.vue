<template>
    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
        <b-card>
            <div slot="header">
                <strong>Existing Pages</strong>
            </div>
            <template v-for="(pages, pageType) in existingPages">
                <template v-for="page in pages">
                    <b-row class="mt-3" :key="pageType +'_' + page.id">
                        <b-button block variant="outline-primary"
                                  @click="$emit('change-visibility', pageType +'_' + page.id)">
                            {{page.page_name}}
                        </b-button>
                    </b-row>
                </template>
            </template>
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
            existingPages: Object
        }
    }
</script>
