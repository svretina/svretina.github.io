import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        description: z.string().optional(),
        date: z.coerce.date(),
        updatedDate: z.coerce.date().optional(),
        heroImage: z.string().optional(),
        draft: z.boolean().default(false),
    }),
});

const projects = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        stack: z.array(z.string()),
        repoUrl: z.string().url(),
        featured: z.boolean().default(false),
        order: z.number().default(99),
    }),
});

export const collections = { blog, projects };
