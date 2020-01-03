<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Add / Edit Pages</strong>
            </b-card-header>
            <b-card-body>
                <edit-page-buttons :existing-pages="existingPages" @change-visibility="visibleForm=$event"/>
                <edit-page-forms :existing-pages="existingPages" :visible-form="visibleForm"/>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import {EventBus} from '@/main'
    import EditPageForms from "./EditPageForms";
    import EditPageButtons from "./EditPageButtons";
    import PageMixin from "@/views/admin-panel/mixins/PageMixin";

    export default {
        components: {EditPageForms, EditPageButtons},
        mixins: [PageMixin],
        data() {
            return {
                existingPages: [],
                visibleForm: ''
            };
        },
        methods: {
            refreshPages() {
                this.getAllPages((pages) => this.existingPages = pages);
            }
        },
        mounted() {
            this.refreshPages();
            EventBus.$on('refresh-pages', this.refreshPages);
        }
    }
</script>