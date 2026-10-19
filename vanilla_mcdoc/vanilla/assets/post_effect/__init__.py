"""Vanilla's assets/post_effect/ files"""
from vanilla_mcdoc.assets.shader.post.InternalTarget import InternalTarget
from vanilla_mcdoc.assets.shader.post.Pass import Pass
from vanilla_mcdoc.assets.shader.post.PostEffect import PostEffect
from vanilla_mcdoc.assets.shader.post.TargetInput import TargetInput
from vanilla_mcdoc.assets.shader.post.UniformValue import UniformValueFloat, UniformValueVec2, UniformValueVec3, UniformValueVec4

BLUR = PostEffect(
    targets={'swap': InternalTarget()},
    passes=[
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In', bilinear=True)],
            output='swap',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='swap', sampler_name='In', bilinear=True)],
            output='minecraft:main',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In', bilinear=True)],
            output='swap',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='swap', sampler_name='In', bilinear=True)],
            output='minecraft:main',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In', bilinear=True)],
            output='swap',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='swap', sampler_name='In', bilinear=True)],
            output='minecraft:main',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=0.0),
                ],
            },
        ),
    ],
)

CREEPER = PostEffect(
    targets={'swap': InternalTarget()},
    passes=[
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/color_convolve',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In')],
            output='swap',
            uniforms={
                'ColorConfig': [
                    UniformValueVec3(name='RedMatrix', type='vec3', value=(0.0, 0.0, 0.0)),
                    UniformValueVec3(name='GreenMatrix', type='vec3', value=(0.3, 0.59, 0.11)),
                    UniformValueVec3(name='BlueMatrix', type='vec3', value=(0.0, 0.0, 0.0)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/bits',
            inputs=[TargetInput(target='swap', sampler_name='In')],
            output='minecraft:main',
            uniforms={
                'BitsConfig': [
                    UniformValueFloat(name='Resolution', type='float', value=16.0),
                    UniformValueFloat(name='MosaicSize', type='float', value=4.0),
                ],
            },
        ),
    ],
)

ENTITY_OUTLINE = PostEffect(
    targets={'swap': InternalTarget()},
    passes=[
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/entity_sobel',
            inputs=[TargetInput(target='minecraft:entity_outline', sampler_name='In')],
            output='swap',
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/entity_outline_box_blur',
            inputs=[TargetInput(target='swap', sampler_name='In', bilinear=True)],
            output='minecraft:entity_outline',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=2.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/entity_outline_box_blur',
            inputs=[TargetInput(target='minecraft:entity_outline', sampler_name='In', bilinear=True)],
            output='swap',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=2.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/blit',
            inputs=[TargetInput(target='swap', sampler_name='In')],
            output='minecraft:entity_outline',
            uniforms={'BlitConfig': [UniformValueVec4(name='ColorModulate', type='vec4', value=(1.0, 1.0, 1.0, 1.0))]},
        ),
    ],
)

INVERT = PostEffect(
    targets={'swap': InternalTarget()},
    passes=[
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/invert',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In')],
            output='swap',
            uniforms={'InvertConfig': [UniformValueFloat(name='InverseAmount', type='float', value=0.8)]},
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/blit',
            inputs=[TargetInput(target='swap', sampler_name='In')],
            output='minecraft:main',
            uniforms={'BlitConfig': [UniformValueVec4(name='ColorModulate', type='vec4', value=(1.0, 1.0, 1.0, 1.0))]},
        ),
    ],
)

SPIDER = PostEffect(
    targets={'large_blur': InternalTarget(), 'small_blur': InternalTarget(), 'temp': InternalTarget(), 'swap': InternalTarget()},
    passes=[
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In', bilinear=True)],
            output='temp',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=15.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='temp', sampler_name='In', bilinear=True)],
            output='large_blur',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=15.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='minecraft:main', sampler_name='In', bilinear=True)],
            output='temp',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(1.0, 0.0)),
                    UniformValueFloat(name='Radius', type='float', value=7.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/box_blur',
            inputs=[TargetInput(target='temp', sampler_name='In', bilinear=True)],
            output='small_blur',
            uniforms={
                'BlurConfig': [
                    UniformValueVec2(name='BlurDir', type='vec2', value=(0.0, 1.0)),
                    UniformValueFloat(name='Radius', type='float', value=7.0),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:post/rotscale',
            fragment_shader='minecraft:post/spiderclip',
            inputs=[
                TargetInput(target='minecraft:main', sampler_name='In'),
                TargetInput(target='large_blur', sampler_name='Blur'),
            ],
            output='temp',
            uniforms={
                'RotScaleConfig': [
                    UniformValueVec2(name='InScale', type='vec2', value=(1.25, 2.0)),
                    UniformValueVec2(name='InOffset', type='vec2', value=(-0.125, -0.1)),
                    UniformValueFloat(name='InRotation', type='float', value=0.0),
                ],
                'SpiderConfig': [
                    UniformValueVec4(name='Scissor', type='vec4', value=(0.0, 0.0, 1.0, 1.0)),
                    UniformValueVec4(name='Vignette', type='vec4', value=(0.1, 0.1, 0.9, 0.9)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:post/rotscale',
            fragment_shader='minecraft:post/spiderclip',
            inputs=[TargetInput(target='small_blur', sampler_name='In'), TargetInput(target='temp', sampler_name='Blur')],
            output='swap',
            uniforms={
                'RotScaleConfig': [
                    UniformValueVec2(name='InScale', type='vec2', value=(2.35, 4.2)),
                    UniformValueVec2(name='InOffset', type='vec2', value=(-1.1, -1.5)),
                    UniformValueFloat(name='InRotation', type='float', value=-45.0),
                ],
                'SpiderConfig': [
                    UniformValueVec4(name='Scissor', type='vec4', value=(0.21, 0.0, 0.79, 1.0)),
                    UniformValueVec4(name='Vignette', type='vec4', value=(0.31, 0.1, 0.69, 0.9)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:post/rotscale',
            fragment_shader='minecraft:post/spiderclip',
            inputs=[TargetInput(target='small_blur', sampler_name='In'), TargetInput(target='swap', sampler_name='Blur')],
            output='temp',
            uniforms={
                'RotScaleConfig': [
                    UniformValueVec2(name='InScale', type='vec2', value=(2.35, 4.2)),
                    UniformValueVec2(name='InOffset', type='vec2', value=(0.45, -4.45)),
                    UniformValueFloat(name='InRotation', type='float', value=45.0),
                ],
                'SpiderConfig': [
                    UniformValueVec4(name='Scissor', type='vec4', value=(0.21, 0.0, 0.79, 1.0)),
                    UniformValueVec4(name='Vignette', type='vec4', value=(0.31, 0.1, 0.69, 0.9)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:post/rotscale',
            fragment_shader='minecraft:post/spiderclip',
            inputs=[TargetInput(target='small_blur', sampler_name='In'), TargetInput(target='temp', sampler_name='Blur')],
            output='swap',
            uniforms={
                'RotScaleConfig': [
                    UniformValueVec2(name='InScale', type='vec2', value=(2.35, 2.35)),
                    UniformValueVec2(name='InOffset', type='vec2', value=(-0.385, -1.29)),
                    UniformValueFloat(name='InRotation', type='float', value=0.0),
                ],
                'SpiderConfig': [
                    UniformValueVec4(name='Scissor', type='vec4', value=(0.0, 0.0, 1.0, 1.0)),
                    UniformValueVec4(name='Vignette', type='vec4', value=(0.31, 0.1, 0.69, 0.9)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:post/rotscale',
            fragment_shader='minecraft:post/spiderclip',
            inputs=[TargetInput(target='small_blur', sampler_name='In'), TargetInput(target='swap', sampler_name='Blur')],
            output='temp',
            uniforms={
                'RotScaleConfig': [
                    UniformValueVec2(name='InScale', type='vec2', value=(2.35, 2.35)),
                    UniformValueVec2(name='InOffset', type='vec2', value=(-0.965, -1.29)),
                    UniformValueFloat(name='InRotation', type='float', value=0.0),
                ],
                'SpiderConfig': [
                    UniformValueVec4(name='Scissor', type='vec4', value=(0.0, 0.0, 1.0, 1.0)),
                    UniformValueVec4(name='Vignette', type='vec4', value=(0.31, 0.1, 0.69, 0.9)),
                ],
            },
        ),
        Pass(
            vertex_shader='minecraft:core/screentriangle',
            fragment_shader='minecraft:post/blit',
            inputs=[TargetInput(target='temp', sampler_name='In')],
            output='minecraft:main',
            uniforms={'BlitConfig': [UniformValueVec4(name='ColorModulate', type='vec4', value=(1.0, 0.8, 0.8, 1.0))]},
        ),
    ],
)
